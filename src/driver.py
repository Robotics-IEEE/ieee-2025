#!/usr/bin/env python3
import rospy
import threading
from geometry_msgs.msg import Twist, Point
from std_msgs.msg import Bool

from utils.motor import Motor
from utils.constructs import *
from utils.level import *
from utils.pathfind import *

#TODO: change "point" to a real data type: UPDATE - use the twist message type.
#TODO: make the publishers publish a legitimate output
    
front_left = Motor(id=3, drivetrain=True)
front_right = Motor(id=4, drivetrain=True)
back_left =  Motor(id=5, drivetrain=True)
back_right = Motor(id=6, drivetrain=True)

ANGULAR_DISTANCE = 1

# TODO: Tune this constant (movement)
MOVEMENT_CONSTANT = 50
# We start at ~12 z
current_pos = Vec2f(0, 12)
angle = 0

magnet_tag = None
tags = [False, False, False, False]
tag_positions = []
score = 0

geodynium_in = 0
nebulite_in = 0

in_cave = False

placed_beacon = False

led_waiting = False  # Waiting for LED?

class Driver:
    def __init__(self, init: bool):
        if init:
            rospy.init_node('driver', anonymous=False)
            self.rate = rospy.Rate(10)

        self.goal_pos_publish = rospy.Publisher('goal_position', Point, queue_size=10)
        self.intake_control_publish = rospy.Publisher('intake_control', Bool, queue_size=10)
        self.outtake_control_publish = rospy.Publisher('outtake_control', Bool, queue_size=10)
        self.shifter_publish = rospy.Publisher('shifter_control', Bool, queue_size=10)

        rospy.Subscriber("goal_status", Bool, self.goal_status_callback)
        rospy.Subscriber("magnet", Bool, self.magnet_callback)
        rospy.Subscriber("shifter_status", Bool, self.shifter_status_callback)
        rospy.Subscriber("vision_vitals", Bool, self.vision_status_callback)

    def goal_position(self, msg: Point):
        self.goal_pos_pub.publish(msg)

    def intake_control(self, msg: Bool):
        self.intake_control_pub.publish(msg)

    def outtake_control(self, msg: Bool):
        self.outtake_control_pub.publish(msg)

    def shifter_control(self, msg: Bool):
        self.shifter_publish_pub.publish(msg)

    def goal_status_callback(self, msg):
        rospy.loginfo(f"Goal Status Received: {msg.data}")

    def magnet_callback(self, msg):
        rospy.loginfo(f"Magnet Status Received: {msg.data}")

    def shifter_status_callback(self, msg):
        rospy.loginfo(f"Shifter Status Received: {msg.data}")

    def vision_status_callback(self, msg):
        rospy.loginfo(f"Vision Status Received: {msg.data}")
    
    def drive_forward_time(self, speed, time=None):
        front_left.move_forward(speed, time)
        front_right.move_forward(speed, time)
        back_left.move_forward(speed, time)
        back_right.move_forward(speed, time)

    def drive_reverse_time(self, speed, time=None):
        front_left.move_reverse(speed, time)
        front_right.move_reverse(speed, time)
        back_left.move_reverse(speed, time)
        back_right.move_reverse(speed, time)

    def drive_forward_position(self, speed, distance=0):
        time = distance * MOVEMENT_CONSTANT

        front_left.move_forward(speed, time)
        front_right.move_forward(speed, time)
        back_left.move_forward(speed, time)
        back_right.move_forward(speed, time)

    def drive_reverse_position(self, speed, distance=0):
        time = distance * MOVEMENT_CONSTANT

        front_left.move_reverse(speed, time)
        front_right.move_reverse(speed, time)
        back_left.move_reverse(speed, time)
        back_right.move_reverse(speed, time)

    def drive_clockwise_time(self, speed, time=None):
        front_left.move_forward(speed, time)
        front_right.move_reverse(speed, time)
        back_left.move_forward(speed, time)
        back_right.move_reverse(speed, time)

    def drive_from_instruction(self, insn: DriveInstruction):
        if insn.get_forwards() == 0:
            # run angle
            self.drive_forward_time(1, insn.get_forwards())
        else:
            self.drive_clockwise_time(1, insn.get_angle())

    def run(self):
        threading.Thread(target=self.goal_position_publish, daemon=True).start()
        threading.Thread(target=self.intake_control_publish, daemon=True).start()
        threading.Thread(target=self.outtake_control_publish, daemon=True).start()
        threading.Thread(target=self.shifter_control_publish, daemon=True).start()

        rospy.spin()

# Policy:
# - Wait for LED to fire
# - First place beacon

# Execute driver
if __name__ == "__main__":
    try:
        level = SimulatedLevel()

        driver = Driver(True)

        # TODO: Get vision
        vision = None

        # place beacon
        target = vision.get_target_pos()
        level.pathfind(current_pos.floor(), target)
        # place_beacon()

        box_target = vision.find_box_pos()
        i = 0
        attempts = 0
        while i < 10:
            closest_ground = vision.find_closest_object()
            if closest_ground is None:
                # rotate 90
                driver.drive_clockwise_time(1, 1)
                i = i - 1
                attempts = attempts + 1
                if attempts is 6:
                    break
            # collect objects
            level.pathfind(current_pos.floor(), closest_ground)

        # go back to box pos
        level.pathfind(current_pos.floor(), box_target)

        # drop_arm()

        # TODO: call the publish functions
    except rospy.ROSInterruptException:
        pass

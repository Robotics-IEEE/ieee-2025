#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from utils.motor import Motor
from utils.constructs import Vec2f
from utils.constructs import *

#TODO: change "point" to a real data type: UPDATE - use the twist message type.
#TODO: make the publishers publish a legitimate output
    
intake = Motor(id=0, drivetrain=False)
outtake = Motor(id=1, drivetrain=False)
indexer = Motor(id=2, drivetrain=False)
front_left = Motor(id=3, drivetrain=True)
front_right = Motor(id=4, drivetrain=True)
back_left =  Motor(id=5, drivetrain=True)
back_right = Motor(id=6, drivetrain=True)

ANGULAR_DISTANCE = 1

# TODO: Tune this constant (movement)
MOVEMENT_CONSTANT = 50
current_pos = Vec2f(0, 0)
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
    def __init__(self):
        rospy.init_node('driver', anonymous=False)
        self.rate = rospy.Rate(10)

    def goal_position_publish(self):
        goal_pos_publish  = rospy.Publisher('goal_position_publish', Point, queue_size=10)
        while not rospy.is_shutdown():
            goal_pos_publish.publish("Output here")
            self.rate.sleep()

    def intake_control_publish(self):
        intake_control_publish  = rospy.Publisher('intake_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            intake_control_publish.publish("Output here")
            self.rate.sleep()

    def outtake_control_publish(self):
        outtake_control_publish  = rospy.Publisher('outtake_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            outtake_control_publish.publish("Output here")
            self.rate.sleep()

    def shifter_control_publish(self):
        shifter_publish  = rospy.Publisher('shifter_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            shifter_publish.publish("Output here")
            self.rate.sleep()

    def goal_status_subscribe():
        rospy.Subscriber("goal_status_publish", "callback?")
        rospy.spin()

    def magnet_subscribe():
        rospy.Subscriber("magnet_publish", "callback?")
        rospy.spin()

    def shifter_status_subscribe():
        rospy.Subscriber("shifter_status_publish", "callback?")
        rospy.spin()

    def vision_status_subscribe():
        rospy.Subscriber("vision_vitals_publish", "callback?")
        rospy.spin()

def tick_odo(angle: float) -> Vec2f:
    nx = math.cos(angle) * ANGULAR_DISTANCE
    nz = math.sin(angle) * ANGULAR_DISTANCE

    return Vec2f(nx, nz)

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

# Policy:
# - Wait for LED to fire
# - First place beacon

# Execute driver
if __name__ == "__main__":
    try:
        driver = Driver()
        # TODO: call the publish functions
    except rospy.ROSInterruptException:
        pass

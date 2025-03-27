#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
from utils.motor import Motor

class VelocityToIntake():

    def __init__(self):
        rospy.init_node("velocity_to_intake", anonymous=False)
        self.rate = rospy.Rate(10)
        # TODO: fix this id 
        self.intake_motor = Motor(id=4, drivetrain=False) 

        # TODO: fix the speed
        self.speed = 1000

    def intake_callback(self, msg):
        if msg.data:
            # Turn on the intake
            self.intake_motor.move_forward(speed=self.speed)
        else:
            self.intake_motor.stop()

    def intake_control_subscribe(self):
        rospy.Subscriber("intake_control", Bool, self.intake_callback)
        rospy.spin()

# Execute velocity to intake
if __name__ == "__main__":
    try:
        velocity_to_intake = VelocityToIntake()
        # Run the publishers and subscribers here
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
from utils.motor import Motor

class VelocityToIntake():

    def __init__(self):
        rospy.init_node("velocity_to_intake", anonymous=False)
        # TODO: fix this id 
        self.intake_motor = Motor(id=4, drivetrain=False) 

        # TODO: fix the speed
        self.speed = 1000
        rospy.Subscriber("intake_control", Bool, self.intake_callback)

    def intake_callback(self, msg):
        if msg.data:
            # Turn on the intake
            self.intake_motor.move_forward(speed=self.speed)
        else:
            self.intake_motor.stop()


# Execute velocity to intake
if __name__ == "__main__":
    try:
        velocity_to_intake = VelocityToIntake()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

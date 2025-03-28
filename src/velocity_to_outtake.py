#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
from utils.motor import Motor

class VelocityToOuttake():

    def __init__(self):
        rospy.init_node("velocity_to_outtake", anonymous=False)
        # TODO: fix this id
        self.outtake_motor = Motor(id=4, drivetrain=False) 

        # TODO: fix the speed
        self.speed = 1000
        rospy.Subscriber("outtake_control", Bool, self.outtake_callback)

    def outtake_callback(self, msg):
        if msg.data:
            # Turn on the outtake
            self.outtake_motor.move_forward(speed=self.speed)
        else:
            self.outtake_motor.stop()


# Execute velocity to intake
if __name__ == "__main__":
    try:
        velocity_to_outtake = VelocityToOuttake()
        velocity_to_outtake.outtake_callback()

    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
import rospy

class VelocityToOuttake():

    def __init__():
        rospy.init_node("velocity_to_outtake", anonymous=False)

    def outtake_control_subscribe():
        rospy.Subscriber("outtake_control_publish", "callback?")
        rospy.spin()

# Execute velocity to outtake
if __name__ == "__main__":
    try:
        velocity_to_outtake = VelocityToOuttake()
        # Run the publishers and subscribers here
    except rospy.ROSInterruptException:
        pass

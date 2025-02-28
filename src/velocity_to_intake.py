#!/usr/bin/env python3
import rospy

class VelocityToIntake():

    def __init__():
        rospy.init_node("velocity_to_intake", anonymous=False)

    def intake_control_subscribe():
        rospy.Subscriber("intake_control_publish", "callback?")
        rospy.spin()

# Execute velocity to intake
if __name__ == "__main__":
    try:
        velocity_to_intake = VelocityToIntake()
        # Run the publishers and subscribers here
    except rospy.ROSInterruptException:
        pass

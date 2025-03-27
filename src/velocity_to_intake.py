#!/usr/bin/env python3
import rospy

class VelocityToIntake():

    def __init__():
        rospy.init_node("velocity_to_intake", anonymous=False)

    def intake_callback(self, msg):
        if msg.data:
            # Turn on the intake
            intake.run()

    def intake_control_subscribe(self):
        rospy.Subscriber("intake_control", self.intake_callback)
        rospy.spin()

# Execute velocity to intake
if __name__ == "__main__":
    try:
        velocity_to_intake = VelocityToIntake()
        # Run the publishers and subscribers here
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
import rospy

class VelocityToDrive():

    def __init__(self):
        rospy.init_node("velocity_to_drive", anonymous=False)
        self.rate = rospy.Rate(10)

    def goal_status_publish(self):
        shifter_publish = rospy.Publisher("goal_status_publish", "status_type", queue_size=10)
        while not rospy.is_shutdown():
            self.rate.sleep()

    def goal_position_subscribe():
        rospy.Subscriber("goal_position_publish", "callback?")
        rospy.spin()

    def odometry_subscribe():
        rospy.Subscriber("odometry_publish", "callback?")
        rospy.spin()

# Execute velocity to drive
if __name__ == "__main__":
    try:
        velocity_to_drive = VelocityToDrive()
        # Run the publishers and subscribers here
    except rospy.ROSInterruptException:
        pass

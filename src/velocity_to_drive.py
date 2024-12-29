import rospy

class VelocityToDrive():

    rate = rospy.Rate(10)
    def __init__():
        rospy.init_node("velocity_to_drive", anonymous=False)

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
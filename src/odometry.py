import rospy

class Odometry():

    rate = rospy.Rate(10)
    def __init__():
        rospy.init_node("odometry", anonymous=False)

    def odometry_publish(self):
        shifter_publish = rospy.Publisher("odometry_publish", "point", queue_size=10)
        while not rospy.is_shutdown():
            self.rate.sleep()
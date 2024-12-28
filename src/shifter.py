import rospy


class Shifter():
    rate = rospy.Rate(10)
    def __init__():
        pass
    
    def shifter_status_publish():
        rospy.init_node("shifter publish", anonymous=False)

        shifter_publish = rospy.Publisher("shifter_status", "status_type", queue_size=10)

        while not rospy.is_shutdown():

            self.rate.sleep()

    def shifter_control_subscribe():
        rospy.init_node("driver_shifter_publish", anonymous=False)
        rospy.Subscriber("shifter_control", "callback?")

        rospy.spin()

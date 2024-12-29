import rospy

class Shifter():
    rate = rospy.Rate(10)

    def __init__():
        rospy.init_node("shifter", anonymous=False)
    
    def shifter_status_publish(self):
        shifter_status_publish = rospy.Publisher("shifter_status_publish", "status_type", queue_size=10)
        while not rospy.is_shutdown():
            self.rate.sleep()

    def shifter_control_subscribe():
        rospy.Subscriber("shifter_control_publish", "callback?")
        rospy.spin()

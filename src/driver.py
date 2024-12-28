import rospy

#TODO: change "point" to a real data type
#TODO: make the publishers publish a legitimate output
class Driver:
    rate = rospy.Rate(10)
    def __init__():
        rospy.init_node('driver', anonymous=False)

    def goal_position_publish(self):
        goal_pos_publish  = rospy.Publisher('goal_position', "point", queue_size=10)
        while not rospy.is_shutdown():
            goal_pos_publish.publish("Output here")
            self.rate.sleep()
        
    def intake_control_publish():
        intake_control_publish  = rospy.Publisher('intake_control', "bool", queue_size=10)
        while not rospy.is_shutdown():
            intake_control_publish.publish("Output here")
            self.rate.sleep()

    def outtake_control_publish():
        outtake_control_publish  = rospy.Publisher('outtake_control', "bool", queue_size=10)
        while not rospy.is_shutdown():
            outtake_control_publish.publish("Output here")
            self.rate.sleep()

    def shifter_publish():
        shifter_publish  = rospy.Publisher('shifter', "bool", queue_size=10)
        while not rospy.is_shutdown():
            shifter_publish.publish("Output here")
            self.rate.sleep()

    def goal_status_subscribe():
        rospy.Subscriber("goal_status", "callback?")
        rospy.spin()
    
    def magnet_subscribe():
        rospy.Subscriber("magnet", "callback?")
        rospy.spin()

    def shifter_status_subscribe():
        rospy.Subscriber("shifter", "callback?")
        rospy.spin()

    def vision_status_subscribe():
        rospy.Subscriber("vision status", "callback?")
        rospy.spin()





    
    

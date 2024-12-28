import rospy

#TODO: change "point" to a real data type
#TODO: make the publishers publish a legitimate output
class Driver:
    rate = rospy.Rate(10)
    def __init__():
        pass

    def goal_position_publish(self):
        goal_pos_publish  = rospy.Publisher('goal_position', "point", queue_size=10)
        rospy.init_node('driver', anonymous=False)
        while not rospy.is_shutdown():
            goal_pos_publish.publish("Output here")
            self.rate.sleep()
        
    def intake_control_publish():
        intake_control_publish  = rospy.Publisher('intake_control', "bool", queue_size=10)
        rospy.init_node('driver', anonymous=False)
        while not rospy.is_shutdown():
            intake_control_publish.publish("Output here")
            self.rate.sleep()

    def outtake_control_publish():
        outtake_control_publish  = rospy.Publisher('outtake_control', "bool", queue_size=10)
        rospy.init_node('driver', anonymous=False)
        while not rospy.is_shutdown():
            outtake_control_publish.publish("Output here")
            self.rate.sleep()

    def shifter_publish():
        shifter_publish  = rospy.Publisher('shifter', "bool", queue_size=10)
        rospy.init_node('driver', anonymous=False)
        while not rospy.is_shutdown():
            shifter_publish.publish("Output here")
            self.rate.sleep()

    def goal_status_subscribe():
        pass
    
    def magnet_subscribe():
        pass

    def shifter_status_subscribe():
        pass

    def vision_status_subscribe():
        pass





    
    

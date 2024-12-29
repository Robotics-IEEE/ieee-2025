#!/usr/bin/env python3
import rospy

#TODO: change "point" to a real data type
#TODO: make the publishers publish a legitimate output
class Driver:
    def __init__(self):
        rospy.init_node('driver', anonymous=False)
        self.rate = rospy.Rate(10)

    def goal_position_publish(self):
        goal_pos_publish  = rospy.Publisher('goal_position_publish', "point", queue_size=10)
        while not rospy.is_shutdown():
            goal_pos_publish.publish("Output here")
            self.rate.sleep()
        
    def intake_control_publish(self):
        intake_control_publish  = rospy.Publisher('intake_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            intake_control_publish.publish("Output here")
            self.rate.sleep()

    def outtake_control_publish(self):
        outtake_control_publish  = rospy.Publisher('outtake_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            outtake_control_publish.publish("Output here")
            self.rate.sleep()

    def shifter_control_publish(self):
        shifter_publish  = rospy.Publisher('shifter_control_publish', "bool", queue_size=10)
        while not rospy.is_shutdown():
            shifter_publish.publish("Output here")
            self.rate.sleep()

    def goal_status_subscribe():
        rospy.Subscriber("goal_status_publish", "callback?")
        rospy.spin()
    
    def magnet_subscribe():
        rospy.Subscriber("magnet_publish", "callback?")
        rospy.spin()

    def shifter_status_subscribe():
        rospy.Subscriber("shifter_status_publish", "callback?")
        rospy.spin()

    def vision_status_subscribe():
        rospy.Subscriber("vision_vitals_publish", "callback?")
        rospy.spin()





    
    

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class Odometry():

    def __init__(self):

        try:
            rospy.init_node("odometry", anonymous=False)
            self.rate = rospy.Rate(10)

        except Exception as e:
            raise

    def odometry_publish(self):
        shifter_publish = rospy.Publisher("odometry_publish", Twist, queue_size=10)

        while not rospy.is_shutdown():
            self.rate.sleep()

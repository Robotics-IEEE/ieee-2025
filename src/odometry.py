#!/usr/bin/env python3
import rospy

class Odometry():

    def __init__(self):
        rospy.init_node("odometry", anonymous=False)
        rate = rospy.Rate(10)

    def odometry_publish(self):
        shifter_publish = rospy.Publisher("odometry_publish", "point", queue_size=10)
        while not rospy.is_shutdown():
            self.rate.sleep()
#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

# TODO: Write logic for reading from modules and publishing

class Odometry():
    """
    Odometry class manages the odometry data received from the robot using the odometry modules,
    translating the data that is received from the modules into a message with angular and linear
    information to be used in other files.
    """
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

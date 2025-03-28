#!/usr/bin/env python3

from utils.constructs import *
import math
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
            pass

    def odometry_publish(self):
        shifter_publish = rospy.Publisher("odometry_publish", Twist, queue_size=10)

        angle = 0

        # easily changable constant
        ANGULAR_DISTANCE = 1

        while not rospy.is_shutdown():
            # read odometry delta
            delta = 1
            nx = math.cos(angle) * ANGULAR_DISTANCE * delta
            nz = math.sin(angle) * ANGULAR_DISTANCE * delta

            shifter_publish.publish(Vec2f(nx, nz))

            self.rate.sleep()

# Execute odometry
if __name__ == "__main__":
    try:
        odometry = Odometry()
        odometry.odometry_publish()
    except rospy.ROSInterruptException:
        pass

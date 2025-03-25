#!/usr/bin/env python3
""" Display magnetometer data at 10Hz """

import rospy
import math
from utils.constructs import *
from std_msgs.msg import Bool

class OdometryToPos():
    """
    Read odometry data and convert to a delta in position using a vector projection based on the angular distance travelled.
    """
    def __init__(self):
        rospy.init_node('odometry_to_pos', anonymous=False)
        self.rate = rospy.Rate(10)  # Hz

    def odometry_to_pos_publish(self):
        # Publish to pos
        publish = rospy.Publisher('pos', Vec2f, queue_size=10)

        # TODO: get angle
        # TODO: get old pos and add
        angle = 0

        # easily changable constant
        ANGULAR_DISTANCE = 1

        while not rospy.is_shutdown():
            # read odometry delta
            delta = 1
            nx = math.cos(angle) * ANGULAR_DISTANCE * delta
            nz = math.sin(angle) * ANGULAR_DISTANCE * delta

            publish.publish(Vec2f(nx, nz))

            self.rate.sleep()

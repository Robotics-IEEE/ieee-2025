#!/usr/bin/env python3

from utils.constructs import *
import math
import rospy
from driver import *
from geometry_msgs.msg import Twist

# It just works.
class DriveForwards():
    def __init__(self):
        try:
            rospy.init_node("drive_forwards", anonymous=False)
            self.rate = rospy.Rate(10)
            self.driver = Driver(False)

        except Exception as e:
            raise e

    def drive_publish(self):
        drive_publish = rospy.Publisher("drive_publish", Twist, queue_size=10)

        self.driver.drive_clockwise_time(1)

        while not rospy.is_shutdown():
            self.rate.sleep()

# Execute odometry
if __name__ == "__main__":
    try:
        drive = DriveForwards()
        drive.drive_publish()
    except rospy.ROSInterruptException:
        pass

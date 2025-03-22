#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from utils.encoder import Encoder
import time

# TODO: Write logic for reading from modules and publishing

class Odometry():
    """
    Odometry class manages the odometry data received from the robot using the odometry modules,
    translating the data that is received from the modules into a message with angular and linear
    information to be used in other files.
    """
    def __init__(self):
        try:
            # TODO: update encoder pins
            self.encoder_back = Encoder(17, 18, 27, 22)
            self.encoder_side_left = Encoder(17, 18, 27, 22)
            self.encoder_side_right = Encoder(17, 18, 27, 22)
            self.position = 0

            rospy.init_node("odometry", anonymous=False)
            self.rate = rospy.Rate(10)

        except Exception as e:
            raise

    def odometry_publish(self):
        odometry_publish = rospy.Publisher("odometry_publish", Twist, queue_size=10)

        # TODO: compute position
        position = Twist()

        while not rospy.is_shutdown():
            try:

                # Read encoder data
                self.encoder_back.update_encoder()
                self.encoder_side_left.update_encoder()
                self.encoder_side_right.update_encoder()

                # Compute position and publish
                odometry_publish.publish(position)
            except Exception as e:
                raise
            
            self.rate.sleep()

# Execute odometry
if __name__ == "__main__":
    try:
        odometry = Odometry()
        odometry.odometry_publish()
    except rospy.ROSInterruptException:
        pass

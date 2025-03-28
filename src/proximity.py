#!/usr/bin/env python3
""" Display proximity data at 10Hz """

import rospy
import Jetson.GPIO as GPIO
from std_msgs.msg import Bool

class Proximity:
    def __init__(self):
        try:
            # Initialize the ROS node
            rospy.init_node('proximity', anonymous=False)
            
            # Set up GPIO pin
            self.pin = 13
            GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
            GPIO.setup(self.pin, GPIO.IN)  # Set pin as input

            self.rate = rospy.Rate(10)  # Hz
        except Exception as e:
            rospy.logerr(f"Failed to initialize sensor: {e}")
            pass

    def proximity_publish(self):   
        # Publish to the proximity topic
        prox_pub = rospy.Publisher('proximity', Bool, queue_size=10)

        while not rospy.is_shutdown():
            try:
                # Read GPIO input
                proximity_detected = GPIO.input(self.pin)
                
                # Publish true if detected, false otherwise
                prox_pub.publish(Bool(data=proximity_detected))
            except Exception as e:
                rospy.logerr(f"Error reading sensor data: {e}")
                pass

            # Sleep for rate of 10Hz
            self.rate.sleep()

# Execute proximity
if __name__ == "__main__":
    try:
        proximity = Proximity()
        proximity.proximity_publish()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        GPIO.cleanup()  # Ensure GPIO is cleaned up properly

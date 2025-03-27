#!/usr/bin/env python3

import rospy
import Jetson.GPIO as GPIO
from std_msgs.msg import Bool

class ProximitySensor:
    """
    Proximity Sensor class reads data from an NPN proximity sensor
    and publishes the detection state to a ROS topic.
    """
    def __init__(self):
        try:
            self.prox_channel = 17  # TODO: Update with actual GPIO pin
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.prox_channel, GPIO.IN)

            # Initialize the ROS node
            rospy.init_node("proximity_sensor", anonymous=False)
            self.pub = rospy.Publisher("proximity_detected", Bool, queue_size=10)

            # Set up event detection for changes
            GPIO.add_event_detect(self.prox_channel, GPIO.BOTH, callback=self.sensor_callback) # TODO: Update with correct RISING/FALL detection

            self.rate = rospy.Rate(10)  # Control loop rate (10Hz)

        except Exception as e:
            rospy.logerr(f"Error initializing ProximitySensor: {e}")

    def sensor_callback(self, channel):
        """
        Callback function triggered on rising/falling edges of the proximity sensor.
        Reads sensor state and publishes it.
        """
        detected = GPIO.input(channel)
        rospy.loginfo(f"Proximity detected: {bool(detected)}")
        self.pub.publish(bool(detected))

    def run(self):
        """
        Keeps the node alive while monitoring the sensor.
        """
        try:
            while not rospy.is_shutdown():
                # Keep the loop alive and allow the callback to handle the code
                self.rate.sleep()
        except KeyboardInterrupt:
            rospy.loginfo("Shutting down proximity sensor node")
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    try:
        prox_sensor = ProximitySensor()
        prox_sensor.run()
    except rospy.ROSInterruptException:
        pass


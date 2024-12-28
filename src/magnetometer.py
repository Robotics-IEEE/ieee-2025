""" Display magnetometer data at 10Hz """

import rospy
import board
import adafruit_lis2mdl
import busio
from std_msgs.msg import Bool

class Magnetometer():
    """ 
    Magnetometer class manages the magnetic sensor near the output of the robot, testing
    if a magnetic piece is detected. This is later used in deciding which box to drop
    the game element into.
    """
    def __init__(self):
        # Initialize the i2c sensor
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
            self.sensor = adafruit_lis2mdl.LIS2MDL(i2c)
            self.rate = rospy.Rate(10) # Hz
        except Exception as e:
            rospy.logerr(f"Failed to initialize sensor: {e}")
            raise

    def magnet_publish(self):
        # Initialize the ROS node
        rospy.init_node('magnetometer', anonymous=False)   

        # Publish to the magnet topic
        mag_pub = rospy.Publish('magnet', Bool, queue_size=10)

        while not rospy.is_shutdown():
            try:
                # Read magnetic data
                mag_x, mag_y, mag_z = self.sensor.magnetic
                mag_found = abs(mag_x) >= 100 or abs(mag_y) >= 100 or abs(mag_z) >= 100

                # Publish true if found, false otherwise
                mag_pub.publish(Bool(data=mag_found))
            except Exception as e:
                rospy.logerr(f"Error reading sensor data: {e}")

            # Sleep for rate of 10Hz
            self.rate.sleep()

# Execute magnetometer
if __name__ == "__main__":
    try:
        magnet = Magnetometer()
        magnet.magnet_publish()
    except rospy.ROSInterruptException:
        pass
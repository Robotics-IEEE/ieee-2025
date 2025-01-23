#!/usr/bin/env python3
import rospy
from custom_types.msg import Status

class Shifter():
    def __init__(self):
        # Initialize the node
        try:
            rospy.init_node("shifter", anonymous=False)
            self.rate = rospy.Rate(10) # Hz
        except Exception as e:
            rospy.logerr(f"Failed to initialize shifter: {e}")
            raise

    def shifter_status_publish(self):
        shifter_publish = rospy.Publisher("shifter_status", Status, queue_size=10)

        while not rospy.is_shutdown():
            try:
                # TODO: Build status type
                # TODO: Fix servo READ code here
                print("hi")
            except Exception as e:
                rospy.logerr(f"Error reading data: {e}")

            # Sleep for rate of 10Hz
            self.rate.sleep()

    def shifter_control_subscribe(self):
        rospy.Subscriber("shifter_control", "callback?")
        # TODO: Fix servo WRITE code here
        # TODO: Make callback 
        rospy.spin()

# Execute shifter
if __name__ == "__main__":
    try:
        shifter = Shifter()
        shifter.shifter_status_publish()
        # Run subscriber, if needed, on other thread or as needed
    except rospy.ROSInterruptException:
        pass

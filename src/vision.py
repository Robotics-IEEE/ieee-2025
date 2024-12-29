#!/usr/bin/env python3
import rospy

class Vision():
    def __init__(self):
        rospy.init_node("velocity_to_drive", anonymous=False)
        self.rate = rospy.Rate(10)

    def vision_vitals_publish(self):
        shifter_publish = rospy.Publisher("vision_vitals_publish", "status_type", queue_size=10)
        while not rospy.is_shutdown():
            self.rate.sleep()

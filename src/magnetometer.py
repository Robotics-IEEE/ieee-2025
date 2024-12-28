import rospy

class Magnetometer():

    def __init__():
        print("Hello")

    def magnet_publish():
        mag_pub = rospy.Publish('magnet', Boolean, queue_size=10)
        rospy.init_node('talker', anonymous=False)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            pub.publish(True)
            rate.sleep()

import rospy

class VelocityToOuttake():

    rate = rospy.Rate(10)
    def __init__():
        rospy.init_node("velocity_to_outtake", anonymous=False)

    def outtake_control_subscribe():
        rospy.Subscriber("outtake_control_publish", "callback?")
        rospy.spin()
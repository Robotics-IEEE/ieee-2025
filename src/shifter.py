import rospy

# TODO: Create status_type

class Shifter():    
    def __init__(self):
        # Initialize the node
        try:
            self.rate = rospy.Rate(10) # Hz
            rospy.init_node("shifter", anonymous=False)
        except Exception as e:
            rospy.logerr(f"Failed to initialize shifter: {e}")
            raise

    def shifter_status_publish(self):
        shifter_publish = rospy.Publisher("shifter_status", status_type, queue_size=10)

        while not rospy.is_shutdown():
            try:
                # TODO: Build status type
                # TODO: Fix dynamixel READ code here
                print("hi")
            except Exception as e:
                rospy.logerr(f"Error reading data: {e}")

            # Sleep for rate of 10Hz
            self.rate.sleep()

    def shifter_control_subscribe(self):
        rospy.Subscriber("shifter_control", "callback?")
        # TODO: Fix dynamixel WRITE code here
        # TODO: Make callback
        rospy.spin()

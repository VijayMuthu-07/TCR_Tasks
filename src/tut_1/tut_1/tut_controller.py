#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TutController(Node):
    
    def __init__(self):
        super().__init__("tut_controller")
        self.sub = self.create_subscription(Pose, "/turtle1/pose", self.callback, 10)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.get_logger().info("TutController has been initiated")

    def callback(self, pos: Pose):
        msg = Twist()
        if pos.x > 9.0 or pos.x < 2.0 or pos.y > 9.0 or pos.y < 2.0:
            msg.linear.x = 1.0
            msg.angular.z = 0.9
        else:
            msg.linear.x = 3.0
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TutController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
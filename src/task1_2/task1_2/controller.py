#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Controller(Node):
    
    def __init__(self):
        super().__init__("controller")
        self.sub = self.create_subscription(String, "image_raw", self.sub_callback, 10)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

    def sub_callback(self, msg: String):
        cmd = Twist()

        match msg.data:
            case "right":
                cmd.linear.x = 2.0
                self.get_logger().info("Moving right")
            case "left":
                cmd.linear.x = -2.0
                self.get_logger().info("Moving left")
            case _:
                cmd.linear.x = 0.0
                self.get_logger().info("Stationary")

        self.pub.publish(cmd)
    
def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
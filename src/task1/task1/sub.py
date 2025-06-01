#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Sub(Node):
    
    def __init__(self):
        super().__init__("sub")
        self.cpu_sub = self.create_subscription(Float32, "/CPU", self.cpu_callback, 10)
        self.temp_sub = self.create_subscription(Float32, "/temp", self.temp_callback, 10)
        
    def cpu_callback(self, msg: Float32):
        usage = msg.data
        if 0.5 <= usage < 1.00:
            self.get_logger().warn("LOW CPU USAGE")
        elif 1.0 <= usage <= 2.00:
            self.get_logger().info("Normal CPU USAGE")
        elif usage > 2.0:
            self.get_logger().fatal("Critical CPU USAGE")
            rclpy.shutdown()

    def temp_callback(self, msg: Float32):
        temp = msg.data
        if temp < 19.0:
            self.get_logger().warn("Low Temperature")
        elif temp > 60.0:
            self.get_logger().fatal("Time to buy a new Pi")
            rclpy.shutdown()
        else:
            self.get_logger().info("Normal Temperature")

def main(args=None):
    rclpy.init(args=args)
    node = Sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Util(Node):

    def __init__(self):
        super().__init__("util")
        self.timer = self.create_timer(1.0, self.monitor)
        self.topics = ["/CPU", "/temp"]

    def monitor(self):
        for topic in self.topics:
            pubs_info = self.get_publishers_info_by_topic(topic)
            pubs = len(pubs_info)

            subs_info = self.get_subscriptions_info_by_topic(topic)
            subs = len(subs_info)

            self.get_logger().info(f"Topic '{topic}': {pubs} publishers, {subs} subscribers")

        nodes = self.get_node_names()
        self.get_logger().info(f"Total active nodes: {len(nodes)}")

def main(args=None):
    rclpy.init(args=args)
    node = Util()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

class Pub(Node):
    
    def __init__(self):
        super().__init__("pub")
        self.cpu_pub = self.create_publisher(Float32, "/CPU", 10)
        self.temp_pub = self.create_publisher(Float32, "/temp", 10)
        self.timer = self.create_timer(1.0, self.pub_stats)

    def pub_stats(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu = Float32()
        cpu.data = cpu_usage
        self.cpu_pub.publish(cpu)
        self.get_logger().info(f"CPU Usage: {cpu.data}%")

        temps = psutil.sensors_temperatures()
        temp = -1.0
        if 'k10temp' in temps:
            for t in temps['k10temp']:
                if t.label == 'Tctl':
                    temp = t.current
                    break
        temp_c = Float32()
        temp_c.data = temp
        self.temp_pub.publish(temp_c)
        if temp != -1.0:
            self.get_logger().info(f"CPU Temp: {temp_c.data}°C")
        else:
            self.get_logger().info("CPU Temp: unavailable")

def main(args=None):
    rclpy.init(args=args)
    node = Pub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
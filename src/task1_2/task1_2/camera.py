#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np

class Camera(Node):

    def __init__(self):
        super().__init__("camera")
        self.pub = self.create_publisher(String, "image_raw", 10)
        self.cap = cv2.VideoCapture(0)
        self.timer = self.create_timer(0.1, self.pub_callback)
        self.center = None
    
    def free(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def pub_callback(self):
        ret, frame = self.cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        direction = "stationary"
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 500:
                x, y, w, h = cv2.boundingRect(largest)
                cx, cy = x + w//2, y + h//2
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.circle(frame, (cx, cy), 0, (0, 0, 255), 5)

                if self.center is not None:
                    dx = cx - self.center
                    direction = "right" if dx > 10 else "left" if dx < -10 else "stationary"

                self.center = cx 

        msg = String()
        msg.data = direction
        self.pub.publish(msg)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) == ord('q'):
            self.free()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = Camera()
    rclpy.spin(node)
    node.free()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
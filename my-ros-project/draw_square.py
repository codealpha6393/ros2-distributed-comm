#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleController(Node):
    def __init__(self):
        super().__init__('square_drawer')
        # We publish to the '/turtle1/cmd_vel' topic to control the turtle
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_turtle)
        self.state = 0 # 0 = Move Forward, 1 = Turn
        self.counter = 0

    def move_turtle(self):
        msg = Twist()

        if self.state == 0:
            # Move Forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info('Moving Forward...')
            self.counter += 1
            if self.counter >= 2: # Move for 2 cycles
                self.state = 1
                self.counter = 0

        elif self.state == 1:
            # Turn 90 Degrees (approximate)
            msg.linear.x = 0.0
            msg.angular.z = 1.57  # Radians (~90 degrees)
            self.get_logger().info('Turning...')
            self.counter += 1
            if self.counter >= 1: # Turn for 1 cycle
                self.state = 0
                self.counter = 0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
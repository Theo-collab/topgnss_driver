import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String

from .hardware_interface import position

class GnssPublisher(Node):

    def __init__(self):
        super().__init__('gnss_publisher')
        self.publisher_ = self.create_publisher(String, 'gnss/position', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        location = position()
        msg.data = f"Position: {location}"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    gnss_publisher = GnssPublisher()

    rclpy.spin(gnss_publisher)

    gnss_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

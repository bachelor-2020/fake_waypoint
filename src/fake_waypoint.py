#!/usr/bin/env python

# Fake WaypointReached message

import rospy

from mavros_msgs.msg import WaypointReached
from std_msgs.msg import Header


class WaypointNode:
    def __init__(self):
        rospy.init_node("waypoint_reached_node")
        self.publisher = rospy.Publisher(
            "mission/reached", WaypointReached, queue_size=1
        )
        self.timer = rospy.Timer(rospy.Duration(0.005), self.timer_callback)

        self.rate = rospy.Rate(0.1)

    def timer_callback(self, event):
        msg = WaypointReached()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "fake"

        msg.wp_seq = 1

        self.publisher.publish(msg)


if __name__ == "__main__":
    try:
        wp_node = WaypointNode()
        while not rospy.is_shutdown():
            wp_node.rate.sleep()

    except rospy.ROSInterruptException:
        pass

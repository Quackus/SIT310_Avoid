#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

rospy.init_node('avoid_1', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.data)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    if data.data < 10:
        vel_msg.linear.x = -2
        rospy.loginfo('Avoid front')
    else:
        vel_msg.linear.x = 2
        
    pub.publish(vel_msg)

def listener():
    rospy.Subscriber('US_Front', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

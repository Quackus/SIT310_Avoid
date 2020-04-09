#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

rospy.init_node('avoid_3', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

left = 100
right = 100

# eventually i'll go back to using an array format
def getLeft(data):  
     global left
     left = data.data
     
def getRight(data):
    global right
    right = data.data

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.data)
    global left
    global right
    threshold = 13
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    if left < threshold or right < threshold:   #if either side reading is too close
        if left <= right:        # if left is closer than right
            vel_msg.angular.z = 2
            rospy.loginfo('Avoid left')
        else:
            vel_msg.angular.z = -2
            rospy.loginfo('Avoid right')
    elif data.data < threshold:
        vel_msg.linear.x = -2
        rospy.loginfo('Avoid front')
    else:
        vel_msg.linear.x = 2
        
    pub.publish(vel_msg)

def listener():
    rospy.Subscriber('US_Left',  Int16,  getLeft)
    rospy.Subscriber('US_Right',  Int16,  getRight)
    rospy.Subscriber('US_Front', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

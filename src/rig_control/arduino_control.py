#!/usr/bin/env python


import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
import numpy as np


pub = rospy.Publisher('temperature', String, queue_size=1000)

def callback(data):
    rate = rospy.Rate(10)
    print "New message received"
    rospy.loginfo(data.data)



    pub.publish(data.data)
    rospy.loginfo(rospy.get_time())
    print "Last message published"
    rate.sleep()


def main():

    rospy.init_node('arduino_control', anonymous=True)

    rospy.Subscriber('temp', String, callback)
#    rospy.Subscriber('motor_cmd', String, callback)
    rospy.spin()

if __name__ == '__main__':
    print "Running"
    main()

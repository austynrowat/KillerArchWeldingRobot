#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " shows %s", data.data)

def listner():

    rospy.init_node('arduino', anonymous=True)

    rospy.Subscriber("temp", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listner()

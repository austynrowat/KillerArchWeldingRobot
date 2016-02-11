#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from irig.msg import IntArray
import numpy


def callback(data):


    global adjusted_data
    adjusted_data = numpy.asarray(data.data) + 1000

    rospy.loginfo(rospy.get_caller_id() + " shows %s", adjusted_data)

def listener():

    rospy.init_node('prof_ctrl', anonymous=True)
    rospy.Subscriber("profile_data", IntArray,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

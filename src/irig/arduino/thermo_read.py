#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

def publisher():
    pub = rospy.Publisher('temp', String, queue_size=10)
    rospy.init_node('temp_sensor', anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        random.seed
        temp_str = "Temp = %s" %random.randint(0,50)
        rospy.loginfo(temp_str)
        pub.publish(temp_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

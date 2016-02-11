#!/usr/bin/env python

import rospy                                #Needed for ROS
from std_msgs.msg import String             #For use of string messages


def publisher():                                                    #
    pub = rospy.Publisher('prof_cmd',String, queue_size=10)       # Declares a Publisher Node with name motor_cmd
    rospy.init_node('command', anonymous=True)                    # Will give node a unique name by adding a number to end

    rate = rospy.Rate(1)                             #For looping at a given Hz

    while not rospy.is_shutdown():              #
        motor_str = "Hello"             #
        rospy.loginfo(motor_str)                #Will print string, write to Node's log file and rosout
        pub.publish(motor_str)                  #Publsihes string to topic
        rate.sleep()                            #Delays so each loop is long enough to keep Rate at desired Hz

if __name__ == '__main__':                      #
    try:                                        #
        publisher()                             #
    except rospy.ROSInterruptException:         #
        pass                                    #

#!/usr/bin/env python


import rospy
from irig.msg import IntArray
from std_msgs.msg import String



def publisher():
    pub = rospy.Publisher('profile_data', IntArray, queue_size=10)
    rospy.init_node('profilometer', anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        profile = IntArray()
        profile.data = [53962, 54407, 54845, 55281, 55721, 56164, 56610, 57045, 57490, 57925, 58371, 58814, 59253, 59692, 60133, 60576, 61017, 61459, 61902, 62343, 62793, 63183, 63604, 64028, 64452, 64875, 65302, 195, 620, 1058, 1493, 1936, 2440, 3006, 3449, 3894, 4342, 4780, 5222, 5667, 6112, 6555, 6999, 7444, 7888, 8326, 8779, 9221, 9666, 10117, 10558, 11002, 11447, 11907, 3712, 4672, 5632, 6592, 7552, 8512, 9472, 10432, 11392, 12352, 13312, 14272, 15232, 16192, 17152, 18112, 19072, 20032, 20992, 21952, 22912, 23872, 24832, 25792, 26752, 27712, 28672, 29632, 30592, 31552, 32512, 33472, 34432, 35392, 36352, 37312, 38272, 39232, 40192, 41152, 42112, 43072, 44032, 44992, 45952, 46912, 47872, 48832, 49792, 50752, 51712, 52672, 53632, 15872, 49328, 16712, 3092, 8326, 4252, 17232, 2272, 2048, 41022, 4114, 38468, 584, 4, 2080, 24668, 17170, 280, 16552]
        pub.publish(profile)
        rospy.loginfo(profile.data)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

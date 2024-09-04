#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('first_ROS_topic', String, queue_size=10)
    rospy.init_node('talker', anonymous=True) # el nodo creado tendrá nombre único
    rate = rospy.Rate(0.5) # 10 Hz

    while not rospy.is_shutdown():
        msg_str = "[LOG] Hola grupo de robotica %s" % rospy.get_time()
        rospy.loginfo(msg_str)
        pub.publish(msg_str)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterrumptException:
        pass


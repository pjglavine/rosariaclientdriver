#!/usr/bin/env python
import roslib
import rospy
import math
import time
import socket
import tf
import serial
from std_msgs.msg import String

def ReachGPS_Publisher():
    pub = rospy.Publisher('ReachGPS', String, queue_size=10)
    rospy.init_node('ReachGPS_Publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    # TCP_IP = '192.168.2.15' REAL REACH TCP_IP
    TCP_IP = '127.0.0.1' #TEST IP
    TCP_PORT = 8889
    BUFFER_SIZE = 1000
    rospy.sleep(7)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while not rospy.is_shutdown():

	GPSdata = s.recv(BUFFER_SIZE)
        rospy.loginfo(GPSdata)
        pub.publish(GPSdata)
        rate.sleep()

if __name__ == '__main__':
    try:
        ReachGPS_Publisher()
    except rospy.ROSInterruptException:
        pass


#!/usr/bin/env python
import roslib
import rospy
import math
import time
import socket
import tf
import serial
from std_msgs.msg import String

def ReachIMU_Publisher():
    pub = rospy.Publisher('ReachIMU', String, queue_size=10)
    rospy.init_node('ReachIMU_Publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
   # TCP_IP = '192.168.2.15'
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFFER_SIZE = 84

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while not rospy.is_shutdown():

	IMUdata = s.recv(BUFFER_SIZE)

	while 1:
	    if not IMUdata:
		break
	    temp = IMUdata[-1]
	    if temp.isdigit():
		break
	    else:
	        IMUdata = IMUdata[:-1]

        rospy.loginfo(IMUdata)
        pub.publish(IMUdata)
        #rate.sleep()

if __name__ == '__main__':
    try:
        ReachIMU_Publisher()
    except rospy.ROSInterruptException:
        pass


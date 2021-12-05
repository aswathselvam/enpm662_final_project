  #! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import tf2_ros
import geometry_msgs.msg

from gazebo_msgs.srv import GetLinkState 
  
model_info= rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)  


br = tf2_ros.TransformBroadcaster()
t = geometry_msgs.msg.TransformStamped()
loop_rate = rospy.Rate(10)

while not rospy.is_shutdown():
    chassis_info = model_info("robot::base_link","world")

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "base_link"
    t.transform.translation.x = chassis_info.link_state.pose.position.x
    t.transform.translation.y = chassis_info.link_state.pose.position.y
    t.transform.translation.z = chassis_info.link_state.pose.position.z
    t.transform.rotation.x = chassis_info.link_state.pose.orientation.x
    t.transform.rotation.y = chassis_info.link_state.pose.orientation.y
    t.transform.rotation.z = chassis_info.link_state.pose.orientation.z
    t.transform.rotation.w = chassis_info.link_state.pose.orientation.w

    br.sendTransform(t)
    loop_rate.sleep()
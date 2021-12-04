#! /usr/bin/env python


import traceback

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
import tf

from gazebo_msgs.srv import GetLinkState 
from gazebo_msgs.msg import LinkState # For getting information about link states

import numpy as np
import math

width = {"fr":0.275, "fl":0.275, "rr":0.275, "rl":0.275}
length = {"fr":0.575, "fl":0.575, "rr":0.575, "rl":0.575}

fr_pub = None
fl_pub = None
rr_pub = None
rl_pub = None

def cmdVelCB(data):
  
  global fr_pub, fl_pub, rr_pub, rl_pub

  mat = np.matrix([[ 1, 1,  (width["fr"] + length["fr"])],
                              [ 1, -1, -(width["fl"] + length["fl"])],
                              [ 1, -1,  (width["rr"] + length["rr"])],
                              [ 1,  1, -(width["rl"] + length["rl"])]])  

  cmd_vel = np.matrix([data.linear.x, data.linear.y, data.angular.z])

  wheel_vel = (np.dot(mat, cmd_vel.T).A1).tolist()

  wv = Float64()

  wv.data = wheel_vel[0]
  fr_pub.publish(wv)

  wv.data = wheel_vel[1]
  fl_pub.publish(wv)

  wv.data = wheel_vel[2]
  rr_pub.publish(wv)

  wv.data = wheel_vel[3]
  rl_pub.publish(wv)
  

def process():

  global fr_pub, fl_pub, rr_pub, rl_pub, model_info, chassis_info

  loop_rate = rospy.Rate(1)

  fr_pub = rospy.Publisher('/front_right_controller/command', Float64, queue_size=10)
  fl_pub = rospy.Publisher('/front_left_controller/command', Float64, queue_size=10)
  rr_pub = rospy.Publisher('/rear_right_controller/command', Float64, queue_size=10)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=10)

  shoulder_angle = rospy.Publisher('/shoulder_angle/command', Float64, queue_size=1)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=1)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=1)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=1)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=1)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=1)

  mouse_sub = rospy.Subscriber('/cmd_vel', Twist, cmdVelCB, queue_size=10)


  br = tf2_ros.TransformBroadcaster()
  t = geometry_msgs.msg.TransformStamped()

  while not rospy.is_shutdown():
    chassis_info = model_info("robot::base_link","world")
    shoulder_link = model_info("robot::shoulder_link","world")
    upper_arm_link = model_info("robot::upper_arm_link","world")
    forearm_link = model_info("robot::forearm_link","world")
    wrist_1_link = model_info("robot::wrist_1_link","world")
    wrist_2_link = model_info("robot::wrist_2_link","world")
    wrist_3_link = model_info("robot::wrist_3_link","world")

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

    shoulder_link = model_info("robot::shoulder_link","base_link")
    upper_arm_link = model_info("robot::upper_arm_link","shoulder_link")
    forearm_link = model_info("robot::forearm_link","upper_arm_link")
    wrist_1_link = model_info("robot::wrist_1_link","forearm_link")
    wrist_2_link = model_info("robot::wrist_2_link","wrist_1_link")
    wrist_3_link = model_info("robot::wrist_3_link","wrist_2_link")
    
    orientation_q = upper_arm_link.link_state.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = tf.transformations.euler_from_quaternion (orientation_list)
    print("r :",math.degrees(roll),"p: ",math.degrees(pitch),"y: ",math.degrees(yaw))
    #shoulder_angle.publish(yaw)

    br.sendTransform(t)
    loop_rate.sleep()




if __name__ == '__main__':
  rospy.init_node('test_mecanum_robot', anonymous=False)
  model_info= rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)  

  try:
    process()

  except Exception as ex:
    print(traceback.print_exc())
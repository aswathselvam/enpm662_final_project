#! /usr/bin/env python3


import traceback

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg

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

  global fr_pub, fl_pub, rr_pub, rl_pub

  loop_rate = rospy.Rate(10)

  fr_pub = rospy.Publisher('/front_right_controller/command', Float64, queue_size=10)
  fl_pub = rospy.Publisher('/front_left_controller/command', Float64, queue_size=10)
  rr_pub = rospy.Publisher('/rear_right_controller/command', Float64, queue_size=10)
  rl_pub = rospy.Publisher('/rear_left_controller/command', Float64, queue_size=10)

  mouse_sub = rospy.Subscriber('/cmd_vel', Twist, cmdVelCB, queue_size=10)

  while not rospy.is_shutdown():

    loop_rate.sleep()


def handle_chassis_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "base_link"
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)



if __name__ == '__main__':
  rospy.init_node('test_mecanum_robot', anonymous=False)
  model_info= rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)
  chassis_info = model_info("robot::base_link","world")
  pose =  chassis_info.pose.position.x
  print(pose)

  try:
    process()

  except Exception as ex:
    print(traceback.print_exc())
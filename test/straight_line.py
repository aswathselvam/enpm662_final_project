#! /usr/bin/env python

from numpy.lib.financial import rate
import rospy
from std_msgs.msg import Float64
from sympy import *
import math
from control_msgs.msg import JointControllerState
import time 
import numpy as np

from gazebo_msgs.srv import GetLinkState 

Q1 = 1 
Q2 = 1
Q3 = 1
Q4 = 1
Q5 = 1
Q6 = 1

def rads(x):
    return math.radians(x)

def callback1(data):
    global Q1
    Q1=data.process_value
    return
    
def callback2(data):
    global Q2
    Q2=data.process_value
    return
    
def callback3(data):
    global Q3
    Q3=data.process_value
    return
    
def callback4(data):
    global Q4
    Q4=data.process_value
    return
    
def callback5(data):
    global Q5
    Q5=data.process_value
    return
    
def callback6(data):
    global Q6
    Q6=data.process_value
    return
    

t1, t2, t3, t4, t5, t6 = symbols('t1 t2 t3 t4 t5 t6')



l = 0.575 
w = 0.275
Hpi = Matrix([[-1/(4*(l + w)), 1/(4*(l + w)), 1/(4*(l + w)), -1/(4*(l + w))],
[1/4, 1/4, 1/4, 1/4],
[-1/4, 1/4, -1/4, 1/4],
])
'''
Jbase = 
Jarm = 
'''

'''
Je = Matrix([Jbase Jarm])
'''

s = 1e-20

J11 = (sin(t1)*sin(t2))/100000000000000000000 - (42500000000000000001*sin(t1))/100000000000000000000 - (1569*cos(t2)*sin(t1))/4000 - (3397500000000000001*cos(t1))/50000000000000000000 + (cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 - (sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 + (cos(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 - (sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 + (cos(t2)*sin(t1)*sin(t3))/100000000000000000000 + (cos(t3)*sin(t1)*sin(t2))/100000000000000000000 + (sin(t1)*sin(t2)*sin(t3))/100000000000000000000 - (cos(t2)*cos(t3)*sin(t1))/100000000000000000000
J12 = (cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 - (1569*cos(t1)*sin(t2))/4000 - (cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 - (cos(t1)*cos(t2))/100000000000000000000 + (sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 + (cos(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 + (cos(t1)*sin(t2)*sin(t3))/100000000000000000000 - (cos(t1)*cos(t2)*cos(t3))/100000000000000000000 - (cos(t1)*cos(t2)*sin(t3))/100000000000000000000 - (cos(t1)*cos(t3)*sin(t2))/100000000000000000000
J13 = (cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 - (cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 + (cos(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000
J14 = (cos(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000
J15 = (cos(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/5000000000 - (cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/5000000000 + (sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/5000000000 + (sin(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/5000000000
J16 = s

J21 = (42500000000000000001*cos(t1))/100000000000000000000 - (3397500000000000001*sin(t1))/50000000000000000000 + (1569*cos(t1)*cos(t2))/4000 - (cos(t1)*sin(t2))/100000000000000000000 - (cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 - (cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 - (sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)))/100000000000000000000 - (cos(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))))/50000000000000000000 - (sin(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))))/50000000000000000000 - (cos(t1)*sin(t2)*sin(t3))/100000000000000000000 + (cos(t1)*cos(t2)*cos(t3))/100000000000000000000 - (cos(t1)*cos(t2)*sin(t3))/100000000000000000000 - (cos(t1)*cos(t3)*sin(t2))/100000000000000000000
J22 = (cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 - (1569*sin(t1)*sin(t2))/4000 - (cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 - (cos(t2)*sin(t1))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 + (cos(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 + (sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 - (cos(t2)*sin(t1)*sin(t3))/100000000000000000000 - (cos(t3)*sin(t1)*sin(t2))/100000000000000000000 + (sin(t1)*sin(t2)*sin(t3))/100000000000000000000 - (cos(t2)*cos(t3)*sin(t1))/100000000000000000000
J23 = (cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 - (cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 + (cos(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 + (sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 - (cos(t2)*sin(t1)*sin(t3))/100000000000000000000 - (cos(t3)*sin(t1)*sin(t2))/100000000000000000000 + (sin(t1)*sin(t2)*sin(t3))/100000000000000000000 - (cos(t2)*cos(t3)*sin(t1))/100000000000000000000
J24 = (cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 - (cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)))/100000000000000000000 + (sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)))/100000000000000000000 + (cos(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 + (sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000
J25 = (cos(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000 + (sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))))/50000000000000000000
J26 = s

J31 = s
J32 = sin(t2)/100000000000000000000 - (1569*cos(t2))/4000 - (cos(t2)*cos(t3))/100000000000000000000 + (cos(t2)*sin(t3))/100000000000000000000 + (cos(t3)*sin(t2))/100000000000000000000 + (sin(t2)*sin(t3))/100000000000000000000 + (cos(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 - (cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000
J33 = (cos(t2)*sin(t3))/100000000000000000000 - (cos(t2)*cos(t3))/100000000000000000000 + (cos(t3)*sin(t2))/100000000000000000000 + (sin(t2)*sin(t3))/100000000000000000000 + (cos(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 - (cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000
J34 = (cos(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 - (cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000 + (sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))/100000000000000000000 + (sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)))/100000000000000000000
J35 = (cos(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 - (cos(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))))/50000000000000000000 + (sin(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2))))/50000000000000000000
J36 = s


Je = Matrix([[J11, J12, J13, J14, J15, J16],
[J21,J22,J23,J24,J25,J26],
[J31,J32,J33,J34,J35,J36]])

'''
Je = Matrix([[J11, J21, J31],
            [J12, J22, J32],
            [J13, J23, J33],
            [J14, J24, J34],
            [J15, J25, J35],
            [J16, J26, J36]])
print(shape(Je))
'''


'''
inp = Matrix([u1, u2, u3, u4])
Ve = Je*inp

'''



def inverse(J,q):
    Js = J.subs({t1: q[0], t2: q[1], t3: q[2], t4: q[3], t5: q[4], t6: q[5]}).evalf()
    try:
        Jp = ((Js.T*Js)).inv()*Js.T
    except:
        return -1
    return Jp

def J_inv(q):
    global Je
    Js = Je.subs({t1: q[0], t2: q[1], t3: q[2], t4: q[3], t5: q[4], t6: q[5]}).evalf()
    try:
        Jp = ((Js.T*Js)).inv()*Js.T
    except:
        return -1
    return Jp



def controlArm():
    global Q1, Q2, Q3, Q4, Q5, Q6, Hpi, s

    # shoulder, upperarm, forearm, wrist 1, wrsit 2, wrist 3
    # q = Matrix([ [rads(-90)], [rads(-90 + -91/1.571)], [rads(0)], [rads(0)], [rads(0)], [rads(0)]])

    Q = Matrix([[Q1], [Q2], [Q3], [Q4], [Q5], [Q6]])
    V = Matrix([ [6], [100], [6] ])    

    loop_rate = rospy.Rate(10)
        
    while not rospy.is_shutdown():
        # Lock Q2 = rads(-90 + 35/1.571)
        Q = Matrix([[Q1], [rads(-35)], [Q3], [Q4], [Q5], [Q6]])
        q_=J_inv(Q)*V
        

        if(q_==-1):
            q=Q
        elif(len(Q)==len(q_)):
            i=0
            while i<len(q_):
                if q_[i]>pi/10:
                    q_[i]=pi/10
                elif q_[i]<-pi/10:
                    q_[i]=-pi/10
                i+=1

            q=Q+q_
        else:
            continue

        print(q_)
        pub_shoulder.publish(q[0]) 
        pub_upperarm.publish(rads(-90 + 35/1.571)) 
        pub_elbow.publish(q[2]) 
        pub_wrist1.publish(q[3])  
        pub_wrist2.publish(q[4]) 
        pub_wrist3.publish(q[5]) 
        
        loop_rate.sleep()

if __name__=="__main__":
    rospy.init_node("arm_ik")
    rospy.Subscriber("/shoulder_pan_joint_position_controller/state/", JointControllerState, callback1, queue_size=5)
    rospy.Subscriber("/shoulder_lift_joint_position_controller/state", JointControllerState, callback2)
    rospy.Subscriber("/elbow_joint_position_controller/state", JointControllerState, callback3)
    rospy.Subscriber("/wrist_1_joint_position_controller/state", JointControllerState, callback4)    
    rospy.Subscriber("/wrist_2_joint_position_controller/state", JointControllerState, callback5)
    rospy.Subscriber("/wrist_3_joint_position_controller/state", JointControllerState, callback6)


    pub_shoulder = rospy.Publisher('/shoulder_pan_joint_position_controller/command', Float64, queue_size=5) 
    pub_upperarm = rospy.Publisher('/shoulder_lift_joint_position_controller/command', Float64, queue_size=5) 
    pub_elbow = rospy.Publisher('/elbow_joint_position_controller/command', Float64, queue_size=5) 
    pub_wrist1 = rospy.Publisher('/wrist_1_joint_position_controller/command', Float64, queue_size=5) 
    pub_wrist2 = rospy.Publisher('/wrist_2_joint_position_controller/command', Float64, queue_size=5) 
    pub_wrist3 = rospy.Publisher('/wrist_3_joint_position_controller/command', Float64, queue_size=5) 

    i=0
    q = Matrix([ [rads(45.001)], [rads(-90 + -80/1.571)], [rads(0.001)], [rads(0.1)], [rads(0.1)], [rads(0.1)]])
    prate = rospy.Rate(10)
    while i<1e1:
        pub_shoulder.publish(q[0]) 
        pub_upperarm.publish(rads(-90 + 35/1.571)) 
        pub_elbow.publish(q[2]) 
        pub_wrist1.publish(q[3])  
        pub_wrist2.publish(q[4]) 
        pub_wrist3.publish(q[5]) 
        i+=1
        prate.sleep()

    controlArm()


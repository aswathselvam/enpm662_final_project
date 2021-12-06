
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


z1 = Matrix([[0, 0, 1]])
z2 = Matrix([[-sin(t1), cos(t1), 0]])
z3 = Matrix([[-sin(t1), cos(t1), 0]])
z4 = Matrix([[-sin(t1), cos(t1), 0]])
z5 = Matrix([[-sin(t1), cos(t1), 0]])
z6 = Matrix([[sin(t5)*(cos(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))) - cos(t5)*(cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)) - sin(t4)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3))), sin(t5)*(cos(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) + sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))) - cos(t5)*(cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - sin(t4)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1))), sin(t5)*(cos(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)) + sin(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3))) - cos(t5)*(cos(t4)*(cos(t2)*cos(t3) - sin(t2)*sin(t3)) - sin(t4)*(cos(t2)*sin(t3) + cos(t3)*sin(t2)))] ])

Je = Matrix([[J11, J12, J13, J14, J15, J16],
[J21,J22,J23,J24,J25,J26],
[J31,J32,J33,J34,J35,J36]])


def J_inv(q):
    global Je
    Js = Je.subs({t1: q[0], t2: q[1], t3: q[2], t4: q[3], t5: q[4], t6: q[5]}).evalf()
    try:
        Jp = (Js.T*Js).inv()*Js.T
    except:
        return -1
    return Jp

import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty
from geometry_msgs.msg import Twist


msg = """
Control Your Toy!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 10
speedy = 10
turn = 10

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('car_teleop')
    
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    x = 0
    y = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_speedy = 0
    control_turn = 0
    rate = rospy.Rate(20) 
    try:
        print(msg)
        print(vels(speed,turn))
        vel_msg = Twist()
        while not rospy.is_shutdown():
            key = getKey()
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            if key in moveBindings.keys():
                if(key == 'i' or key == ','):
                    x = moveBindings[key][0]
                elif(key == 'j' or key=='l'):
                    y = moveBindings[key][1]
                elif(key == 'u' or key=='o'):
                    th = moveBindings[key][1]

                count = 0
            elif key in speedBindings.keys():
                #speed = speed * speedBindings[key][0]
                #speedy = speedy * speedBindings[key][0]
                #turn = turn * speedBindings[key][1]
                count = 0

                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            elif key == ' ' or key == 'k' :
                x = 0
                y = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    y = 0
                    th = 0
                if (key == '\x03'):
                    break

            target_speed = speed * x
            target_speedy = speedy * y
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 10)
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 10 )
            else:
                control_speed = target_speed

            if target_speedy > control_speedy:
                control_speedy = min( target_speedy, control_speedy + 10)
            elif target_speedy < control_speedy:
                control_speedy = max( target_speedy, control_speedy - 10 )
            else:
                control_speedy = target_speedy

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 10 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 10 )
            else:
                control_turn = target_turn

            vel_msg.linear.x = control_speed
            vel_msg.linear.y = control_speedy
            vel_msg.angular.z = control_turn

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

                ind = wheel_vel>10
                wheel_vel[ind] = 10
                
                ind = wheel_vel <-10
                wheel_vel[ind]=-10

                q=Q+q_
            else:
                continue

            print("speed: ",control_speed, "speed: ",control_speedy, "speed: ",control_turn)
            velocity_publisher.publish(vel_msg)

            rate.sleep()


    except Exception as e:
        print(e)



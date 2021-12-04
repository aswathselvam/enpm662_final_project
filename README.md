# Robot Arm:

## Documents:
Link to report, discussions are [here](https://drive.google.com/drive/folders/1Rp32GsWSPNQBrzzu0iJeZsF_Ti1MLDRo?usp=sharing)

## Setup
If running ROS Noetic, you might have to run this command in the terminals you open:
```
mkdir ~/bin
PATH=~/bin:$PATH
ln -s /usr/bin/python3 ~/bin/python
```

## Universal Robot Arm
Clone the Universial Robotics [repoitory](https://github.com/ros-industrial/universal_robot) to your workspace. Or install 

# Enpm662 Final Project
---

Mecanum Wheel [FM202-205-15U-R/L (FUJI)](http://www.fuji-bearing.com/japanese/products/conveyor/conveyor0408.html)
gazebo model description.

![](https://user-images.githubusercontent.com/26181834/129763254-aa74e592-cdbe-4859-87d8-fd93592cd40e.png)

## Usage

How to build fuji mecanum in your robot.

```xml
<?xml version="1.0" ?>
<robot name="mecanum_wheel_robot" xmlns:xacro="http://ros.org/wiki/xacro">

  ....

  <!-- include mecanum_wheel macro -->
  <xacro:include filename="$(find enpm662_final_project)/urdf/mecanum_wheel_macro.xacro" />
  <!-- load macro -->
  <!-- name: link name -> ${name}_wheel_link -->
  <!-- side: mecanum wheel direct 1: right, -1: left -->
  <xacro:mecanum_wheel name="right" side="1" />
  <xacro:mecanum_wheel name="left" side="1" />

  <joint name="right_joint_name" type="fixed">    
    <parent link="parent" />
    <child link="right_wheel_link" />
  </joint>

  <joint name="left_joint_name" type="fixed">    
    <parent link="parent" />
    <child link="left_wheel_link" />
  </joint>

  ....

</robot>
```

## Test

- Gazebo simulation

  ![mecanum_robot](https://user-images.githubusercontent.com/26181834/129851426-2e3568eb-f340-41ce-9c6a-84ec9c883126.gif)

  ```bash
  # Gazebo GUI launch
  $ roslaunch enpm662_final_project gazebo_test_robot.launch
  ```

  ```bash
  # mecanum control node
  $ rosrun enpm662_final_project test_mecanum_robot.py
  ```

  ```bash
  # Teleop control node
  $ rosrun enpm662_final_project test_publisher.py
  ```

  ```bash
  $ rostopic pub /cmd_vel geometry_msgs/Twist "linear:
    x: 1.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0" 
  ```

## Data visualization with Rqt
Ex: To plot wrist 1 joint setpoint and angle data, in Rviz, open plot and choose:
/wrist_1_joint_position_controller/command/data
/wrist_1_joint_position_controller/state/process_value

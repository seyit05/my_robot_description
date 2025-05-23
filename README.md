# my_robot_description
 
![image](https://github.com/user-attachments/assets/02e6894b-1940-4a2c-b978-3cbc0218de89)

![image](https://github.com/user-attachments/assets/aaef56a3-8038-40c2-b88c-838872b6883f)

🦾 my_robot_description

This package provides a description of a mobile robot designed for use in the ROS 2 Humble environment. It defines the robot's physical structure, joints, and sensor placements using URDF/Xacro format. It also includes configurations for visualizing the robot in RViz2.

📁 Directory Structure

my_robot_description/

├── launch/

│   └── display.launch.py         # Launch file to visualize the robot in RViz2

├── rviz/
│   └── my_robot.rviz             # RViz2 configuration file

├── urdf/
│   └── my_robot.urdf.xacro       # Robot description in Xacro format

├── package.xml

├── CMakeLists.txt

└── README.md

🚀 Installation & Build

Clone the package into your ROS 2 workspace:


cd ~/ros2_ws/src

git clone https://github.com/seyit05/my_robot_description.git

Install dependencies:

cd ~/ros2_ws

rosdep install --from-paths src --ignore-src -r -y

Build the workspace:


colcon build

source install/setup.bash

🧪 Usage

To launch the robot model in RViz2:


ros2 launch my_robot_description display.launch.py

🔧 Features

ROS 2 Humble compatibility

Modular robot description using Xacro

RViz2 visualization support

Integrated with robot_state_publisher and joint_state_publisher_gui

🧱 Requirements

ROS 2 Humble (Ubuntu 22.04)

Required ROS 2 packages:

sudo apt install ros-humble-xacro \
                 ros-humble-joint-state-publisher-gui \
                 ros-humble-robot-state-publisher \
                 ros-humble-rviz2

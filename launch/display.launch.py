from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command

import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path(
        'my_robot_description'), 
        'urdf', 
        'main.xacro')
    
    rviz_config_path = os.path.join(get_package_share_path(
        'my_robot_description'), 
        'rviz', 
        'urdf_config.rviz')
    
    
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
    )

    pkg_share = FindPackageShare(package='my_robot_description').find('my_robot_description')
    control_yaml = os.path.join(pkg_share, 'config', 'my_robot_control.yaml')

    # ROS 2 Control Parametrelerini Yükle
    load_control_params = launch_ros.actions.Node(
        package="ros2_control_node",
        executable="ros2_control_node",
        parameters=[control_yaml],
        output="screen"
    )

    # Controller Spawner (ROS 2 Control)
    controller_spawner = launch_ros.actions.Node(
        package="controller_manager",
        executable="spawner",
        output="screen",
        arguments=[
            "joint_state_controller",
            "front_left_drive_controller",
            "front_right_drive_controller",
            "rear_left_drive_controller",
            "rear_right_drive_controller",
            "front_left_steer_controller",
            "front_right_steer_controller",
            "rear_left_steer_controller",
            "rear_right_steer_controller"
        ]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )


    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
        load_control_params,
        controller_spawner
    ])
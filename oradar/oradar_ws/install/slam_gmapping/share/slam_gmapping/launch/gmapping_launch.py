#!/usr/bin/env python3

import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='False')
    return LaunchDescription([

        Node(
            package='slam_gmapping',
            node_namespace='slam_gmapping',
            node_executable='slam_gmapping',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}]
        ),
    ])

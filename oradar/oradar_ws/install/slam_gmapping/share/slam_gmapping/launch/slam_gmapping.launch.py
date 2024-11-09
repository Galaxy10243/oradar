from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
import launch.actions
import launch_ros.actions
from launch_ros.actions import Node
import os
import launch
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='false')
    return LaunchDescription([

        Node(
            package='slam_gmapping',
            node_namespace='transform',
            node_executable='transform',
            output='screen',
            parameters=[{'parents_frame': "odom",
                         'child_frame': "laser",
                         'x': 0.1,
                         'y': 0.2,
                         'z': 0.5,
                         'roll': 0.0,
                         'pitch': 0.0,
                         'yaw': 0.0}],
        ),
        Node(
            package='tf2_ros',
            node_namespace='laser_to_base_link',
            node_executable='static_transform_publisher',
            output='screen',
            arguments = [ '0', 
            			  '0', 
            			 '1', 
            			 '0', 
            			  '0', 
            			  '0', 
            			  'laser', 
            			 'base_link']

        ),
        
        Node(
            package='rviz2',
            node_namespace='map_rviz',
            node_executable='rviz2',
            output='screen',
            arguments = [ '-d', "/home/yahboom/oradar_ws/src/slam_gmapping/rviz/map_view.rviz"],
        )
        
      
    ])

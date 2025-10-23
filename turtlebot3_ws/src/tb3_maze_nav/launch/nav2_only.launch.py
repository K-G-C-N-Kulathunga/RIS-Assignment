from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg = FindPackageShare('tb3_maze_nav')
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('nav2_bringup'), 'launch', 'bringup_launch.py'])
        ),
        launch_arguments={
            'params_file': PathJoinSubstitution([pkg, 'config', 'nav2_tb3.yaml']),
            'use_sim_time': 'true'
        }.items()
    )
    return LaunchDescription([nav2])

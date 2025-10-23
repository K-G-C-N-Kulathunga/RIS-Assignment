from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg = FindPackageShare('tb3_maze_nav')
    world = PathJoinSubstitution([pkg, 'worlds', 'maze.world'])

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    tb3_gazebo_pkg = FindPackageShare('turtlebot3_gazebo')
    spawn_tb3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([tb3_gazebo_pkg, 'launch', 'spawn_turtlebot3.launch.py'])
        )
    )

    return LaunchDescription([gazebo, spawn_tb3])

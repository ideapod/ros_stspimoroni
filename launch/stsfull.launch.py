from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stspimoroni',
            executable='sts',
            name='transport'
        ),
        Node( 
            package='v4l2_camera',
            executable=' ',
            parameters=[
            {'-p': 'image_size:="[640,480]"'}
            ],
            name='camera'
        )
    ])
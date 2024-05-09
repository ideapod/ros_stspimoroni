# ros_stspimoroni
python ros2 package to support using the sts pi moroni kit

# Setting up the Pi
This package was tested on Raspberry pi 3, [ubuntu 22.04.3 LTS for Pi](https://ubuntu.com/download/raspberry-pi), [Ros2 Iron](https://docs.ros.org/en/iron/index.html). set up ubuntu and install iron. 


Based on the [pimoroni sts pi moroni kit](https://core-electronics.com.au/pimoroni-sts-pi-build-a-roving-robot.html), 
the [explorerhat pro](https://shop.pimoroni.com/products/explorer-hat?variant=1074827129) uses the [explorerhat package](https://github.com/pimoroni/explorer-hat), so be sure to pip install that package.

The package requires access to gpio pins which normally requires root. To gain access use:

`sudo apt install rpi.gpio-common`

`sudo adduser "${USER}" dialout`

`sudo reboot`

# Video feed
The Pi camera is incorporated into the sts pi moroni kit and the camera is compatible with the video4linux project. Refer to [Articuled Robotics #9 - Adding a Camera](https://articulatedrobotics.xyz/mobile-robot-9-camera)

pre requisites:
`sudo apt install libraspberrypi-bin v4l-utils ros-iron-v4l2-camera ros-iron-image-transport-plugins`


Connect up the ribbon cable, and reboot the pi. to check the video is there and working do:

`vcgencmd get_camera`

you should see: 
`supported=1 detected=1`

then try:
`v4l2-ctl --list-devices`
you should see:
`...`
`mmal service 16.1 (platform:bcm2835-v4l2):
	/dev/video0`

my final test was:
`ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 out.jpg`
and this put out a picture from the camera. 

once all that is working, you should be right to start the ros camera node on pi.

# Usage
`ros2 run stspimoroni sts`

will run the main ros2 node that responds to geometry_msgs/msg/Twist messages like those put out by teleop_twist_keyboard

on your desktop run:

`ros2 run teleop_twist_keyboard teleop_twist_keyboard` 

OR for joystick:

`ros2 run joy joy_node`

and you can drive it around

The camera node is started with: 
`ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]"`

to see the images on your desktop run the rqt image viewer: 
`ros2 run rqt_image_view rqt_image_view
`

# Launch file
I've included a launch file which will launch both nodes:
`ros2 launch stspimoroni sts`

from your desktop you can then run the image viewer and the teleop node and control the robot and move it around while monitoring video. 

# TODO
debug why the camera isn't reliable.  
stream it to twitch/youtube so it's out of the ros realm. 


# Acknowledgements

The code for the ROS node comes from Sid Faber's [Robots repository](https://github.com/SidFaber/robots) and his [excellent youtube series](https://youtu.be/xHw2WFe6GBs?si=untW6XQJD278Ds5q)

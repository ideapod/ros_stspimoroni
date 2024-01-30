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

# Usage
`ros2 run stspimoroni sts`

will run the main ros2 node that responds to geometry_msgs/msg/Twist messages like those put out by teleop_twist_keyboard

on your desktop run:

`ros2 run teleop_twist_keyboard teleop_twist_keyboard` 

and you can drive it around

# TODO
working on a launch file that will get the camera going.  

# Acknowledgements

The code for the ROS node comes from Sid Faber's [Robots repository](https://github.com/SidFaber/robots) and his [excellent youtube series](https://youtu.be/xHw2WFe6GBs?si=untW6XQJD278Ds5q)

# ros_stspimoroni
python ros2 package to support using the sts pi moroni kit

# Setting up the Pi
This package was tested on Raspberry pi 3, ubuntu 22.04.3 LTS.

Based on the [pimoroni sts pi moroni kit](https://core-electronics.com.au/pimoroni-sts-pi-build-a-roving-robot.html), 
the [explorerhat pro](https://shop.pimoroni.com/products/explorer-hat?variant=1074827129) uses the [explorerhat package](https://github.com/pimoroni/explorer-hat)

this package requires access to gpio pins which normally requires root. To gain access use:

`sudo apt install rpi.gpio-common`
`sudo adduser "${USER}" dialout`
`sudo reboot`

# Usage
`ros2 run stspimoroni sts`

will run the main ros2 node that allows movement. 

# TODO
working on a launch file that will get the camera going.  

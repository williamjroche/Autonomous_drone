# Autonomous Drone
This is an Autonomous Drone that uses Computer vision to fly with radio transmission override. This GitHub repo has two main file systems, a flight controller file system and flight computer. This is an ongoing project and the flight controller is currently in development.

Flight Controller:
- Connects to IMU and adjusts motor speed for flight stability using PID control
- Implements PID control (a feedback control system that continuously adjusts an output to reach a target value)
- Holds main motor control software
- Custom Transmitter/Receiver interface program


Flight Computer:
- Uses ROS2 for giving commands to the flight controller based on computer vision input
- Holds main computer vision software
- Interfaces with camera

Drone Frame:
- Modified STL's I found online, made to be 3D printed using PLA
- All screw holes are designed for M3 scews, holes are not threaded so use nuts
- Due to 3D printer tolerences, some holes may not work with M3 scews, in that case I've used M2 screws with nut and lock washer
- Make sure all screws are as tight as you can get them or you will lose strength in the frame

How to use:


*This repo is best used as a guide for making your own custom autonomous drone, considering the implementation is very specific to the materials I am using*
- All files in "Flight Controller" should be downloaded to a Raspberry Pi Pico running the latest micropython
- Use GPIO pins listed in "esc_control.py" or change the values in the code to your needs
- Ensure the BLDC motors that are next to each other rotate in different directions
- [Directions for Flight Computer are a work in progress]


*This is a work in progress*


MIT License

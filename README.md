# Autonomous Drone
This is an Autonomous Drone that uses Computer vision to fly with radio transmission override. This GitHub repo has two main file systems, a flight controller file system and flight computer.

Flight Controller:
- Connects to IMU and adjusts motor direction and speed for flight stability
- Holds main esc control
- Implements PID control (a feedback control system that continuously adjusts an output to reach a target value)

Flight Computer:
- Uses ROS2 for giving commands to the flight controller based on computer vision input
- Holds main computer vision software
- Interfaces with camera

How to use:


*This repo is best used as a guide for making your own custom autonomous drone, considering the implementation is very specific to the materials I am using*
- All files in "Flight Controller" should be downloaded to a Raspberry Pi Pico running the latest micropython
- Use GPIO pins listed in "esc_control.py" or change the values in the code to your needs
- Ensure the BLDC motors that are next to each other rotate in different directions
- [Directions for Flight Computer are a work in progress]


*This is a work in progress*


MIT License

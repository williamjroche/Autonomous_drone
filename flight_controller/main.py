# MIT License
# Created by: William Roche III
# GitHub: @ williamjroche
from esc_control import ESCcontrol
from imu_icm20948 import IMU
from controller_input import DroneController
#from pid import PID
import time

#initialization and arming the ESCs/motor
esc = ESCcontrol()
#initialize IMU
imu = IMU()
#esc.esc_calibrate() #for first time use, ESCs need to be calibrated --> uncomment this line of code-->take off propellors-->run file-->delete this line of code
esc.esc_arm()

control = DroneController()
yaw = control.get_yaw()
control.print_values()
pitch = control.get_pitch()
roll = control.get_roll()

#test motor
#esc.esc_speed(1500000, 1)
#time.sleep(5)
#esc.stop_motor(1)

#while True:
    #imu.update()
    #imu.test()
while True:
    throttle = control.get_throttle()
    control.print_values()
    esc.esc_speed(throttle, 5)
    time.sleep(0.5)
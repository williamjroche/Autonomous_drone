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

while True:
    imu.update()
    imu.test()
    throttle = control.get_throttle()
    pitch = control.get_pitch()
    roll = control.get_roll()
    yaw = control.get_yaw()
    control.print_values()
    
    #copies so we don't overwrite actual values
    roll_cmd = roll
    pitch_cmd = pitch
    
    roll_correction = roll_cmd * 0.3   #30% correction
    pitch_correction = pitch_cmd * 0.3
    
    #motor speed adjustment
    motor1_speed = throttle - pitch_correction + roll_correction
    motor2_speed = throttle - pitch_correction - roll_correction
    motor3_speed = throttle + pitch_correction - roll_correction
    motor4_speed = throttle + pitch_correction + roll_correction
    
    #convert to normalized values (-1 to 1)
    motor1_speed = max(-1, min(1, motor1_speed))
    motor2_speed = max(-1, min(1, motor2_speed))
    motor3_speed = max(-1, min(1, motor3_speed))
    motor4_speed = max(-1, min(1, motor4_speed))
    
    esc.esc_speed(motor1_speed, 1)
    esc.esc_speed(motor2_speed, 2)
    esc.esc_speed(motor3_speed, 3)
    esc.esc_speed(motor4_speed, 4)
    
    time.sleep(0.02) #updates at 50Hz
import qwiic_icm20948
import time
import sys
from machine import Pin, I2C
import math


class IMU:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
        self.IMU = qwiic_icm20948.QwiicIcm20948()

        if self.IMU.connected == False:
            raise Exception("IMU not connected!")
    
        self.IMU.begin()
        print("IMU initialized successfully")
        
        self.roll = 0.0
        self.pitch = 0.0
    
    def update(self):
        #Read sensors, calculate angles
        self.IMU.getAgmt()
        #Convert raw values to g's (assuming ±2g range, 16-bit: 32768 = 2g)
        self.ax = self.IMU.axRaw / 16384.0  # Scale factor for ±2g
        self.ay = self.IMU.ayRaw / 16384.0
        self.az = self.IMU.azRaw / 16384.0
        #Convert raw gyro to degrees/second (assuming ±250°/s range)
        self.gx = self.IMU.gxRaw / 131.0  # Scale factor for ±250°/s
        self.gy = self.IMU.gyRaw / 131.0
        self.gz = self.IMU.gzRaw / 131.0
        #Magnetometer (scale varies, typical: 0.15 µT/LSB)
        self.mx = self.IMU.mxRaw * 0.15
        self.my = self.IMU.myRaw * 0.15
        self.mz = self.IMU.mzRaw * 0.15
        # Return roll, pitch, yaw
        self.roll = math.atan2(self.ay, self.az) * (180 / math.pi)
        self.pitch = math.atan2(-self.ax, math.sqrt(self.ay*self.ay + self.az*self.az)) * (180 / math.pi)
        
    
    def get_roll(self):
        return self.roll
    
    def get_pitch(self):
        return self.pitch
    
    def test(self):
        #Prints accelerometer, gyroscope, magnetometer
        print(f"Roll: {self.roll:.2f}, Pitch: {self.pitch:.2f} degrees")
        print("-------------")
        time.sleep(0.05)

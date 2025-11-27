# MIT License
# Created by: William Roche III
# GitHub: @ williamjroche
from machine import Pin, PWM
import time

class ESCcontrol:
    def __init__(self):
        self.min_throttle = 1000000
        self.max_throttle = 2000000
        self.pwm_frequency = 50
        #ESC1 - GPIO15
        self.esc1 = PWM(Pin(15))
        self.esc1.freq(self.pwm_frequency)
        
        #ESC2 - GPIO14
        self.esc2 = PWM(Pin(14))
        self.esc2.freq(self.pwm_frequency)
        
        #ESC3 - GPIO13
        self.esc3 = PWM(Pin(13))
        self.esc3.freq(self.pwm_frequency)
        
        #ESC4 - GPIO12
        self.esc4 = PWM(Pin(12))
        self.esc4.freq(self.pwm_frequency)
        
        #list for control of all motors
        self.all_escs = [self.esc1, self.esc2, self.esc3, self.esc4]
    
    def esc_calibrate(self):
        #set all esc to min throttle
        for esc in self.all_escs:
            esc.duty_ns(self.min_throttle)
        time.sleep(2)
        #set all esc to max throttle
        for esc in self.all_escs:
            esc.duty_ns(self.max_throttle)
        time.sleep(2)
        #set all esc to min throttle
        for esc in self.all_escs:
            esc.duty_ns(self.min_throttle)
        time.sleep(2)
    
    def esc_arm(self):
        for esc in self.all_escs:
            esc.duty_ns(self.min_throttle)
        time.sleep(2)
    
    def stop_motor(self, esc):
        for esc in self.all_escs:
            esc.duty_ns(0)
    
    def esc_speed(self, normalized, motor_select):
        #map motor_select cases to the motor objects
        motor_map = {
            1: [self.esc1],
            2: [self.esc2],
            3: [self.esc3],
            4: [self.esc4],
            5: self.all_escs
        }
        duty_select = int((1500 + (500 * (normalized)))*1000)
        
        #find the motors to control based on the selection
        motors_to_control = motor_map.get(motor_select)
        #error handling
        if motors_to_control is None:
            print(f"Invalid motor: {motor_select}")
        #send speed to esc
        for esc in motors_to_control:
            esc.duty_ns(duty_select)
                
        time.sleep(0.01)

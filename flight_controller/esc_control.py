from machine import Pin, PWM
import time

min_throttle = 1000000
max_throttle = 2000000
pwm_frequency = 50
esc1 = None
esc2 = None
esc3 = None
esc4 = None
all_escs = []

def esc_init():
    global esc1, esc2, esc3, esc4, all_escs
    #ESC and the GPIO pin it is connected to -- tells the controller where to send the PWM signal
    esc1 = PWM(Pin(15))
    esc1.freq(pwm_frequency)
    
    #ESC 2 on Pin 14 [Placeholder pin]
    esc2 = PWM(Pin(14))
    esc2.freq(pwm_frequency)
    
    #ESC 3 on Pin 13 [Placeholder pin]
    esc3 = PWM(Pin(13))
    esc3.freq(pwm_frequency)
    
    #ESC 4 on Pin 12 [Placeholder pin]
    esc4 = PWM(Pin(12))
    esc4.freq(pwm_frequency)
    
    #list for control of all motors
    all_escs = [esc1, esc2, esc3, esc4]


def esc_arm():
    #Set all esc to min throttle
    for esc in all_escs:
        esc.duty_ns(min_throttle)
    time.sleep(2)
    
    
def esc_speed(duty_select, motor_select):
    #map motor_select cases to the motor objects
    motor_map = {
        1: [esc1],
        2: [esc2],
        3: [esc3],
        4: [esc4],
        5: all_escs
    }
    #Find the motors to control based on the selection
    motors_to_control = motor_map.get(motor_select)
    #send speed to esc
    for esc in motors_to_control:
        if esc is not None:
            esc.duty_ns(duty_select)
            
    time.sleep(0.01)


def stop_motor(esc_number):
    for esc_number in all_escs:
        esc_number.duty_ns(0)
    
    
    
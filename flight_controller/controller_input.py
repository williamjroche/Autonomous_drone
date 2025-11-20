# MIT License
# Created by: William Roche III
# GitHub: @ williamjroche
from machine import PWM, Pin
import time
import _thread

class PWMReader:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.IN)
        self.pulse_width = 1500 #default value
        self.last_time = 0
        self.lock = _thread.allocate_lock() #used later in program so only 1 at a time access pulse width
        
        self.pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._irq_handler)
        
    def _irq_handler(self, pin):
        current_time = time.ticks_us()
        
        if pin.value() == 1: #rising edge
            self.last_time = current_time
        else: #falling edge
            if self.last_time > 0:
                pulse = time.ticks_diff(current_time, self.last_time)
                
                if 800 < pulse < 2200: #set pulse defined above to pulse_width, valid PWM in range of 1000-2000 micro sec
                    with self.lock: #self.lock explained above
                        self.pulse_width = pulse
    
    def get_value(self):
        with self.lock: #self.lock explained above
            return self.pulse_width
        
    
    def get_normalized(self, min_val=-1.0, max_val=1.0): #normalizes joysticks to -1 to 1 or different min and max vals
        pulse = self.get_value()
        
        normalized = (pulse - 1500)/500.0 #we defined above that 1500 is default or 0 in our normalized vals
        
        return min_val + (normalized + 1.0) * (max_val - min_val) / 2.0 #offset + scale factor * range --> formula is used for ANY range you want
    

class DroneController:
    def __init__(self):
        self.channels = { #GPIO pins
            'throttle': PWMReader(2),
            'yaw': PWMReader(3),
            'pitch': PWMReader(4),
            'roll': PWMReader(5),
            'f1': PWMReader(6), #extra function
        }
    
    def get_channel(self, channel_name):
        if channel_name in self.channels:
           return self.channels[channel_name].get_value() #return PWM signal from channel
        return 1500 #return our define 0 if channel not found
    
    def get_all_values(self):
        return { #return all PWM signals from all channels
            'throttle': self.get_throttle(),
            'yaw': self.get_yaw(),
            'pitch': self.get_pitch(),
            'roll': self.get_roll(),
            'f1': self.get_channel('f1'),
        }
    
    def get_yaw(self):
        return self.channels['yaw'].get_normalized(-1.0, 1.0) #get yaw value between -1 and 1
    
    def get_roll(self):
        return self.channels['roll'].get_normalized(-1.0, 1.0) #get roll value between -1 and 1
    
    def get_pitch(self):
        return self.channels['pitch'].get_normalized(-1.0, 1.0) #get pitch value between -1 and 1
    
    def get_throttle(self):
        return self.channels['throttle'].get_normalized(0.0, 1.0) #get throttle value between 0 and 1
    
    def get_f1(self):
        return self.channels['f1'].get_normalized(-1.0,1.0) #get f1 value
    
    def print_values(self): #print to terminal for debugging
        values = self.get_all_values()
        print(f"T:{values['throttle']:.2f} Y:{values['yaw']:.2f} "
              f"P:{values['pitch']:.2f} R:{values['roll']:.2f} ")

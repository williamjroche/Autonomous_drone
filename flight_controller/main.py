import esc_control as esc
import time

#initialization and arming the ESCs/motor
esc.esc_init()
#esc.esc_calibrate() #for first time use, ESCs need to be calibrated --> uncomment this line of code-->take off propellors-->run file-->delete this line of code
esc.esc_arm()



#test motor
esc.esc_speed(1500000, 1)
time.sleep(5)
esc.stop_motor(1)
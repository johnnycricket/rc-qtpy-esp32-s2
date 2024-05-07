import board 
import pwmio
import time
from adafruit_motor import motor

a0_pin = board.A0
a1_pin = board.A1
PWN_FREQ = 25
DECAY_MODE = motor.SLOW_DECAY


a0_pwm = pwmio.PWMOut(a0_pin, PWN_FREQ)
a1_pwm = pwmio.PWMOut(a1_pin, PWN_FREQ)

moto = motor.DCMotor(a0_pwm, a1_pwm)
moto.decay_mode = DECAY_MODE

def hardStop(): 
    moto.throttle = 0
    
def acclDeccl(currNotch, newNotch, currDir):

    if(currNotch == newNotch):
        return moto.throttle
    
    # need to: convert notch to 0 to 1.0 for throttle
    # need to: convert notch result to forward or backward

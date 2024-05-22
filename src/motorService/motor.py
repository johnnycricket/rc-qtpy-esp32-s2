import board 
import pwmio
import time
from adafruit_motor import motor

class MotorService:
    PWN_FREQ = 25
    DECAY_MODE = motor.SLOW_DECAY
    a0_pin = board.A0
    a1_pin = board.A1

    a0_pwm = pwmio.PWMOut(pin=a0_pin, frequency=PWN_FREQ)
    a1_pwm = pwmio.PWMOut(pin=a1_pin, frequency=PWN_FREQ)

    moto = motor.DCMotor(a0_pwm, a1_pwm)
    moto.decay_mode = DECAY_MODE

    def fHund(self, i: int): 
        return i/100

    def iHund(self, f: float):
        return int(f*100)

    def hardStop(self): 
        self.moto.throttle = None
    
    def speed(self, newValue: int):
        if type(newValue) is None:
            newValue = 0

        theStep = 2
        currThrottle = self.moto.throttle
        currAsFloat: float = 0.0
        
        if currThrottle != None:
            print('gonna set currAsFloat')
            print(currThrottle)
            currAsFloat = currThrottle
        
        if(currThrottle == self.fHund(newValue)):
            return self.moto.throttle
        print("---------")
        print(newValue)
        print(currAsFloat)
        
        isAcceleration = True if currAsFloat < self.fHund(newValue) else False

        if not isAcceleration: 
            theStep = theStep * -1

        for duty_cycle in range(newValue, self.iHund(currAsFloat), theStep):
            self.moto.throttle = self.fHund(duty_cycle)
            print(self.moto.throttle)
            time.sleep(0.2)

    def getSpeed(self):
        return self.moto.throttle
    
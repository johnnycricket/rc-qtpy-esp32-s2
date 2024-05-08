from motor.motor import MotorService
from reverserEnum import ReverserEnum

class ControlClass:
    def __init__(self, dir = ReverserEnum.NUETRAL):
        self.direction = dir
        self.mc = MotorService
        self.revEnum = ReverserEnum

    def getReverser(self): 
        return self.direction

    def setReverser(self, new):
        self.direction = new
        return self.direction
    
    def setThrottle(self, newSpeed):
        if self.direction == self.revEnum.REVERSE: 
            self.mc.speed(-newSpeed)
        elif self.direction == self.revEnum.FORWARD:
            self.mc.speed(newSpeed)  
        else:
            #assume nuetral
            self.mc.speed(0)
            
    def eStop(self):
        self.mc.hardStop()
        return 'stopped'

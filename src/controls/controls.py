from src.motorService.motor import MotorService
from src.controls.reverserEnum import ReverserEnum

class ControlClass:
    direction = ReverserEnum.NUETRAL
    mc = MotorService()

    def getReverser(self): 
        return self.direction

    def setReverser(self, new):
        self.direction = int(new)
        return self.direction
    
    def setThrottle(self, newSpeed):
        convSpeed = int(newSpeed)
        result: float | None
        print(int(ReverserEnum.REVERSE))
        if self.direction == int(ReverserEnum.REVERSE):
            print('reversing!') 
            result = self.mc.speed(-convSpeed)
        elif self.direction == int(ReverserEnum.FORWARD):
            print('forward!')
            result = self.mc.speed(convSpeed)  
        else:
            #assume nuetral
            print('nuetral')
            result = self.mc.speed(None)
        return result
   
    def eStop(self):
        self.mc.hardStop()
        return 'stopped'

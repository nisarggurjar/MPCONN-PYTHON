# Poly = Multiple (many)
# Morph = Forms

class TwoWheeler:

    def __init__(self):
        self.wheels = 2
        self.max_capactity = 2

    def Direction(self):
        print("Using Handel")


class MotorCycle(TwoWheeler):
    
    def Engine(self):
        print("Petrol Engine")

    def Seat(self):
        print("Leather Cover")    



class XYZbike(MotorCycle):

    def Power(self):
        print("150 cc")

    def FuelCapacity(self):
        print("20 Lts")

class ABCbike(MotorCycle):

    def Engine(self):
        print("Electric Vehicle")


    def FuelCapacity(self):
        print("15 Lts")


tw = TwoWheeler()

# print(tw.wheels)

m = MotorCycle()

bike = XYZbike()

print(bike.wheels)
# bike.Direction()
abc = ABCbike()

m.Engine()
abc.Engine()
bike.Engine()

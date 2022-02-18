# class TwoWheeler:

#     def __init__(self):
#         self.wheels = 2
#         self.max_capactity = 2

#     def Direction(self):
#         print("Using Handel")


# class MotorCycle(TwoWheeler):
    
#     def Engine(self):
#         print("Petrol Engine")

#     def Seat(self):
#         print("Leather Cover")    



# class XYZbike(MotorCycle):

#     def Power(self):
#         print("150 cc")

#     def FuelCapacity(self):
#         print("20 Lts")

# class ABCbike(MotorCycle):

#     def Power(self):
#         print("100 cc")

#     def FuelCapacity(self):
#         print("15 Lts")


# tw = TwoWheeler()

# # print(tw.wheels)

# m = MotorCycle()

# bike = XYZbike()

# print(bike.wheels)
# bike.Direction()

# abc = ABCbike()

# abc.Power()

# bike.Power()


# class Mom:

#     def __init__(self):
#         self.eyes = "black"


# class Dad:

#     def Work(self):
#         print("Software Developer")


# class Child(Mom, Dad):
#     pass

# a = Child()

# print(a.eyes)
# a.Work()


## Hybrid


from turtle import pen


class A:

    def ShowA(self):
        print("A")


class B(A):
    
    def ShowB(self):
        print("B")


class C(B):

    def ShowC(self):
        print("C")


class D(A):

    def ShowD(self):
        print("D")

a = A()

b = B()

c = C()

d = D()

a.ShowA()

b.ShowA()
b.ShowB()

c.ShowA()
c.ShowB()
c.ShowC()

d.ShowA()
d.ShowD()

# Operator Overloading

class A:
    def __init__(self,a,b):
        self.real = a
        self.img = b

    def __add__(self, num2):
        return self.real+num2.real, self.img+num2.img

c1 = A(1,4) # 1+4j

c2 = A(3,2) # 3+2j

c3 = c1 + c2

print(c3) # 4+6j

print(2+3)

print("Hello"+"world")
from abc import ABC, abstractmethod


class A(ABC):

    def add(self, a,b):
        print(a+b)

    def sub(self, a,b):
        print(a-b)

    @abstractmethod
    def div(self, a,b):
        pass

    def mul(self, a,b):
        print(a*b)

class B(A):

    def div(self, a,b):
        print(a/b)
    
    def Power(self, a,b):
        print(a**b)


a = B()

a.Power(3,2)
a.div(10,3)

a.add(3,4)

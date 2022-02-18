
from unicodedata import name


class TestClass:
    name = "Test Class"

    def __init__(self):
        print("Constructor Called")

    def Greet(self):
        print("Hello")
        print(self.name)

a = 5

obj = TestClass()


obj.name = "Test Object"

obj.Greet()

obj2 = TestClass()

# obj.__init__()

# print(obj.name)
# print(obj2.name)

# Cunstructor -> Special type member function
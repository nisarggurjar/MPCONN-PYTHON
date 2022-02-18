
class Human:

    def __init__(self):
        name = input("Enter Your name")
        age = int(input("Enter Your Age"))
        self.name = name
        self.age = age
        
    def Show(self):
        print("Name is", self.name)
        print("age is", self.age)

    def Setter(self):
        name = input("Enter Your name")
        age = int(input("Enter Your Age"))
        self.name = name
        self.age = age

    def Walk(self):
        pass

    def Eat(self):
        pass


# obj1 = Human("Raj", 5.6, 60)
# obj2 = Human("Jeet", 5.4, 70)
# obj3 = Human("Geet", 5.7, 65)

obj1 = Human()
obj2 = Human()
obj3 = Human()

obj1.Setter()
obj1.Show()


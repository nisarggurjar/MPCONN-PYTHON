# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# s = 0 ==> morning, s = 1 ==> Afternoon

def Greet(s):
    if s == 0:
        print("Good Morning")
    elif s == 1:
        print("Good Afternoon")
    else:
        print("Hello")

# a = Greet(43)

# You use functions in programming to bundle a set of instructions that you want to use repeatedly or that, 
# because of their complexity, are better self-contained in a sub-program and called when needed. 
# That means that a function is a piece of code written to carry out a specified task. 
# To carry out that specific task, the function might or might not need multiple inputs. 
# When the task is carried out, the function can or can not return one or more values.

# There are three types of functions in Python:

# Built-in functions, such as help() to ask for help, min() to get the minimum value, print() to print an object to the terminal,… You can find an overview with more of these functions here.
# User-Defined Functions (UDFs), which are functions that users create to help them out; And
# Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.


# Types of User Defined Functions

# No Input No Output

def AddNumber():
    a = int(input("1st number"))
    b = int(input("2nd number"))
    print(a+b)

# AddNumber()

# No Input Yes Output

def AddNumber1():
    a = int(input("1st number"))
    b = int(input("2nd number"))
    return a+b

# ans = AddNumber1()
# print(ans)

# Yes Input No Output

def AddNumber2(a,b):
    print(a+b)


# AddNumber2(123, 345)

# Yes Input Yes Output

def AddNumber3(a,b):
    return a+b

# ans = AddNumber3(12,23)
# print(ans)


# Multiple Returns 

def Calc(a,b):
    return a/b, a*b, a+b, a-b

# A, B, C, D = Calc(10,3)
# print(A,B,C,D)


# an anonymous function may be a function that’s defined without a reputation.
# While defining normal functions, we are using the def keyword in Python, 
# but while defining anonymous functions we are using the lambda keyword.

# A lambda function in python has the subsequent syntax.

# Syntax : lambda arguments: expression

sqr = lambda num: num**2
print(sqr(15))

cube = lambda num: num**3
print(cube(3))

# TODO: filter, map, reduce
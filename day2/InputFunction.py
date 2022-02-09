# The input() method reads the user's input and returns it as a string.
# Syntax : input(prompt)

input()

# input method is used to store data
a = input()
print(a)

# By default the type of data returend by input method is string ('str')
print(type(a))

# We Can Change the type of input data using type casting
a = int(input())

# We can pass any string as argument to show as promt for users
b = float(input("Enter an decimal value : "))
# this promt does not affect the value or type of data entered or returned

name = input("Enter your name")
print(name)
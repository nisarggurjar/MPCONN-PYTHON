# Data type is an attribute associated with a piece of data that tells a computer system how to interpret 
# its value. Understanding data types ensures that data is collected in the preferred format and the value 
# of each property is as expected.


# Integer (int) 
# It is the most common numeric data type used to store numbers without a fractional component (-707, 0, 707).

a1 = 1
b1 = 435
c1 = -34235

# Floating Point (float)
# It is also a numeric data type used to store numbers that may have a fractional component, 
# like monetary values do (707.07, 0.7, 707.00).

a2 = 0.45
b2 = 34.34
c2 = -9.5

# String (str or text)
# It is a sequence of characters and the most commonly used data type to store text. Additionally, 
# a string can also include digits and symbols, however, it is always treated as text. 
# Note : String in python is denoted by double quotes (" ") or single (' ') 

a3 = "python"
b3 = "java"
c3 = 'php'

# Boolean (bool)
# It represents the values true and false. When working with the boolean data type, it is helpful to 
# keep in mind that sometimes a boolean value is also represented as 0 (for false) and 1 (for true). 

a4 = True
b4 = False

# Complex
# A complex number has two parts, real part and imaginary part. Complex numbers are represented as A+Bi or A+Bj , 
# where A is real part and B is imaginary part. Python supports complex data type as built-in feature which means we can 
# directly perform different operations on complex number in python.

a5 = 3+4j
b5 = -3+5j
c5 = -4-7j

# type() function
# type() method returns class type of the argument(object) passed as parameter.

print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))


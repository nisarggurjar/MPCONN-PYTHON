# The print() function in Python is used to print a specified message on the screen. 
# The print command in Python prints strings or objects which are converted to a string while printing on a screen.

print("hello")

a = 5
b = 6

# Using comma operator we can print more than one element at time

print(a,b)

# While printing multiple elements it is not necessary that it should be of same type

a1 = 1
a2 = 3.12
a3 = "Python"

print(a1, a2, a3)

# An escape sequence is a special character used in the form of backslash(\) followed by a character that is required.
# These characters are used to represent whitespace.


# \’	This represents a single quote
# \n	This represents a newline
# \r	This represents a carriage return
# \t	This represents a tab
# \b	This represents a backspace
# \f	This represents a formfeed
# \ooo	This represents an octal value
# \xhh	This represents a hex value
# \\	This represents a backslash
# \uxxxx	This represents 16 bits hex value
# \uxxxxxxxx	This represents 32 bits hex value


print('Nisarg\'s Laptop')

print("Ht there,\nHow are you?")

print("Happy\tCoding")
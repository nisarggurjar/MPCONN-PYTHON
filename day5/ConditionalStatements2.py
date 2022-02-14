## Short Hands

# If you have only one statement to execute, you can put it on the same line as the if statement.

if 5<10: print("5 is greater")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

age = 19
print("You can vote") if age>=18 else print("You can't vote")

# Nested If else
# When an if else statement is present inside the body of another “if” or “else” then this is called nested if else.

# girls, age greater than 16 can vote
# boys, age greater than 18 can vote

age = int(input("Enter Your Age"))
gender = input("Enter your gender") # males -> m, females - f

if gender == 'f':
    if age>=16:
        print("you can vote")
    else:
        print("You cant vote")
elif gender == 'm':
    if age>=18:
        print("you can vote")
    else:
        print("You cant vote")
else:
    print("Enter a valid input")

# Conditional Statement With Logical Operator

age = int(input("Enter Your Age"))
gender = input("Enter your gender") # males -> m, M and for females -> f, F

if ((gender == 'f' or gender == 'F' ) and age>=16) or ((gender == 'm' or gender == 'M' ) and age>=18):
    print("you can vote")
else:
    print("You can't vote")



# Conditional Statement With Membership Operator

languages = ["C", "CPP", "Python", "GOLang", "JS"]

if "JAVA" in languages:
    print("Yes")
else:
    print("No")

# Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions.

# Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome. You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.

# 1	if statements
# An if statement consists of a boolean expression followed by one or more statements.

print("welcome")
a = int(input("Enter any numer"))
if a>10:
    print(a)
print("Thank You!")


# 2	if...else statements
# An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.

print("Hi..")
age = int(input("Enter Your Age"))
if age>=18:
    print("You can vote")
else:
    print("You can't vote")
print("VOTE")


# 3	nested if statements
# You can use one if or else if statement inside another if or else if statement(s).

print("Welcome!")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
op = input("Enter Operator")
if op == '+':
    print("Sum is", num1+num2)
elif op == '-':
    print("diffrence is", num1 - num2)
elif op == '*':
    print("Product is", num1*num2)
elif op == '/':
    print("division is", num1/num2)
else:
    print("Enter a valid operator")
print("Thank You")
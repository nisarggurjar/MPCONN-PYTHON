# Loops -> A loop statement allows us to execute a statement or group of statements multiple times.

# Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.


# A for loop is used for iterating over a sequence.

li = [1,2,3,4,5,6,7,8,9,10]
for i in li: 
    print(i**2)

print("\n")

s = "Hello To All"
for i in s:
    print(i)

students = {"sno":12, "name":"Nisarg", "Subject":["P", "C", "B"]}
for item in students:
    print(students[item])


tup = (1,2,3,4,5,6,7,8,9,10)
for i in tup: 
    print(i**2)

print("\n")

# range() allows the user to generate a series of numbers within a given range. Depending on how many arguments the user is passing to the function, user can decide where that series of numbers will begin and end as well as how big the difference will be between one number and the next.range() takes mainly three arguments.

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,100,2):
    print(i)

print("\n")
# start: integer starting from which the sequence of integers is to be returned
# stop: integer before which the sequence of integers is to be returned. The range of integers end at stop – 1.
# step: integer value which determines the increment between each integer in the sequence

# PATTERNS

#    *
#   **
#  ***
# ****
#*****



space = 4
for i in range(1,6):
    print(space * " ", end = "")
    print("*"*i)
    space-=1


for i in range(1,6):
    for j in range(i):
        print(j+1, end='')
    print("")



# 

li = ["C", "CPP", "Python", "GOLang", "JS"]

for i in range(len(li)):
    print(li[i])
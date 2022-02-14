# With the break statement we can stop the loop even if the while condition is true:

# for i in range(0,20,2):
#     print(i)
#     if i == 11:
#         break

a = True

while a:
    print("Hi..")
    age = int(input("Enter Your Age"))
    if age>=18:
        print("You can vote")
    else:
        print("You can't vote")
    conf = input("Do you want to continue")
    if conf == 'n':
        break # a = False


# With the continue statement we can stop the current iteration, and continue with the next:

a = True
while a:
    a = int(input())
    if a % 2 == 0:
        print("it's an even number")
        continue
    print("it's not an even number, to make it even let's add 1 to it")
    a+=1
    print("Now it's an even number",a)
    conf = input("Do you want to continue")
    if conf == 'n':
        a = False


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

if age>18:
    pass
else:
    pass

for i in range(20):
    print(i)
    if i % 2 == 1:
        pass
    print("hy")
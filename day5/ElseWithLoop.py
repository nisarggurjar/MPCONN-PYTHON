# The else keyword in a loop specifies a block of code to be executed when the loop is finished normally:

for i in range(0,26):
    print("hy", i)
    if i%2==1 and i>15:
        break
else:
    print("LOOP Terminated normally")

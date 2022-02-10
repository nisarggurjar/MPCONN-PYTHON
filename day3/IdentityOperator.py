# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

a = 5 
b = 6
c = 5
l1 = [1,2,3]
l2 = l1
l3 = l1.copy

# is 	Returns True if both variables are the same object	x is y	

print(a is b)
print(a is c)
print(l1 is l2)
print(l1 is l3)
# is not	Returns True if both variables are not the same object	x is not y	

print(a is not b)
print(a is not c)
print(l1 is not l2)
print(l1 is not l3)
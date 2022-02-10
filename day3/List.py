# A list is a container which holds comma-separated values (items or elements) between square brackets 
# where items or elements need not all have the same type.

# In general, we can define a list as an object that contains multiple data items (elements). 
# The contents of a list can be changed during program execution. 
# The size of a list can also change during execution, as elements are added or removed from it.

l1 = [12,2132,3.14, "python", "list", 5+6j]

print(l1)
print(len(l1))  # Checking Length of list
print(type(l1)) # Checking Type of list

# Accessing List with Index

print(l1[2])  
print(l1[-2])

# Slicing of list

print(l1[2:5])
print(l1[:-2])

# Index difference
print(l1[::-1])

# Functions of List

l = [1,2,3,4,5,6,7]

# append(x)	- Adds an item (x) to the end of the list
l.append(8)
print(l)

# pop() - Removes the item at the given position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.
a = l.pop(4)  # Return
print(a)
# print(l)

# insert(i, x) - Inserts an item at a given position. The first argument is the index of the element before which to insert. For example, a.insert(0, x) inserts at the front of the list.
l.insert(1, "Python")
# print(l)

# remove(x)	- Removes the first item from the list that has a value of x. Returns an error if there is no such item.
l.remove("Python")
# l.remove("Python")
print(l)

# index(x) - Returns the position of the first list item that has a value of x. Raises a ValueError if there is no such item.
a = l.index(4) # Return
print(a)

# reverse()	- Reverses the elements of the list in place.
l.reverse()
print(l)

# extend(iterable) - Extends the list by appending all the items from the iterable. This allows you to join two lists together. 
l.extend([1,2,3,4,5,6]) # l = l + [1,2,3,4,5,6]
print(l)

# count(x) - Returns the number of times x appears in the list.
a = l.count(1) # Return
print(a)

l2 = ["python", "c", "java", "go", "ruby"]

# sort(key=None, reverse=False) - Sorts the items of the list in place. The arguments can be used to customize the operation.

l2.sort()
print(l2)

# clear() - Removes all items from the list.
l1.clear()
print(l1)

# copy() - Returns a shallow copy of the list.
l1 = l2.copy() # Shallow # return
l2.append("php")
print(l1)
print(l2)


# Type Casting a String into List
name = "Python is a programming language"
name = list(name)
print(name)
name.sort()
print(name)

print(l2)


# Multidimentional List

# Multi dimensional lists are lists within lists, or lists within lists within lists... 
# you get the point. It can get very confusing very fast, but it is good to know that it is an option. 
# Usually a dictionary will be the better choice rather than a multi-dimensional list in Python, 

l = [[1, "Aditya", ["P", "C", "B"]],[2, "Vaibhav", ["P", "C", "M"]],[3, "Shefali", ["P", "C", "M"]],[4, "Rahul",["P", "C", "B"]]]

# Accessing Multidimentional List
print(l[1][2][-1])
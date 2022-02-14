# A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

t = ("Python", 1, 3.14, "C", (1,34), 1, 1)

print(t) 

# subscriptable : indexing, negative ondexing etc will work
print(t[1])
print(t[-2])
print(t[1:])

# Functions of Set

# count()	Returns the number of times a specified value occurs in a tuple
print(t.count(1))

# index()	Searches the tuple for a specified value and returns the position of where it was found
print(t.index(1))


# Changing / updating Set via type casting
t = list(t)
print(t)
t.append("GO")
t[0] = "PHP"
print(t)
t = tuple(t)
print(t)

t = (1,2)
t2 = (3,4)
t3 = t + t2

print(type(t3))



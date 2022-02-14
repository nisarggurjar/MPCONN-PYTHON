# sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values.
# Because sets cannot have multiple occurrences of the same element, 
# it makes sets highly useful to efficiently remove duplicate values from a list or tuple
# and to perform common math operations like unions and intersections.

s = {"Python", "C", "CPP", "GO", 1, 23, 4.6, "Python"}
print(s)

print(type(s))
print(len(s))


# Functions Of Set

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# Some Examples of Set Functions

s.add("R")
s.add("R")
print(s)


s.remove(4.6)
# s.remove("PHP")

a = s.pop()
print(a)

a = s.pop()
print(a)
print(s)

s1 = {1,2,3,4}
s1.update(s)
print(s1)

set1 = {2,4,5,6}
set2 = {4,6,7,8}

st = set1.union(set2)  # Return
print(st)

st2 = set1.intersection(set2)
print(st2)

s3 = {4,6}

print(set1.issuperset(s1))

print(set1.symmetric_difference(set2))

set1.clear()
print(set1)


x = set2.copy()

x.add("Python")

print(x, set2)

set2.discard(8)
set2.discard(8)

print(set2)

s1 = {1,2,3, {4,5,6, {6,7,8}}}
print(s1)
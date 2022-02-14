# Python Dictionary is used to store the data in a key-value pair format. The dictionary is the data type in Python, 
# which can simulate the real-life data arrangement where some specific value exists for some particular key. 
# It is the mutable data-structure. The dictionary is defined into element Keys and values.

students = {"sno":12, "name":"Nisarg", "Subject":["P", "C", "B"]}

print(students)


# To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.

print(students['Subject'])
name = ("name","class")

d1 = {
    "sno":1,
    name:"Nisarg",
}

print(type(d1))

# You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry

# update existing entry
d1["sno"] = 2 
d1.update({"sno": 2})

# Add new entry
d1.update({"year": 2016, "stream":"CSE"})



a = d1.pop(name)
print(a)
b = d1.popitem()
print(b)
print(d1)
# del(d1)
print(d1)
d2 = d1 # Deep Copy
d3 = d1.copy() # Shallow Copy

# Nested Dictionary
d = {
    "student":{
        "name":"Nisarg",
        "year":"2016"
    },
    "Projects":{
        "major":"Classifier",
        "minor":"IOT Device"
    }
}
print(d['student']['name'])

# Dictionary Functions

# dict.clear()
# Removes all elements of dictionary dict

# 2	dict.copy()
# Returns a shallow copy of dictionary dict

# 3	dict.fromkeys()
# Create a new dictionary with keys from seq and values set to value.

# 4	dict.get(key, default=None)
# For key key, returns value or default if key not in dictionary

# 5	dict.has_key(key)
# Returns true if key in dictionary dict, false otherwise

# 6	dict.items()
# Returns a list of dict's (key, value) tuple pairs

# 7	dict.keys()
# Returns list of dictionary dict's keys

# 8	dict.setdefault(key, default=None)
# Similar to get(), but will set dict[key]=default if key is not already in dict

# 9	dict.update(dict2)
# Adds dictionary dict2's key-values pairs to dict

# 10	dict.values()
# Returns list of dictionary dict's values

# Some Examples

print(students.keys())
print(students.items())
print(students.values())
print(students.get("sno"))
print(students.fromkeys(("sno", "name")))

students.clear()
print(students)


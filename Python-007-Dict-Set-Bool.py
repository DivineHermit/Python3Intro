"""
    Python3 Introduction
    More Data Types: Dictionaries, Sets and Boolean Values.
    Written by: Dominic Lee
    Date: 
"""
print("DICTIONARIES".center(50, "+"))  # Output separator
# Dictionaries are lists consisting of Key & Value pairs, while lists can use an index to access a value,
# with Dictionaries you use the Key.
person = {"name":"Bob", "age":32, "status":"traveling"}
# We have a representation of a person, in this case Bob, lets display Bobs info:
print("*"*20)
print("Name:".ljust(10), person.get("name"))
print("Age:".ljust(10), person.get("age"))
print("Status:".ljust(10), person.get("status"))
print("*"*20)
# By specifying the Key 'name' we get the value 'Bob'.

# We can also access a Dictionary directly using square brackets, similar to slicing.
print(person['name'])

# We can get all the Keys or all the Values with the following methods:
print("Keys".ljust(7), "=", person.keys())
print("Values".ljust(7), "=", person.values())

# Since we lost Bob while covering lists lets update his status:
person["status"] = "M.I.A."
print("Bobs status is:", person.get("status"))

# Lets take a look at the methods available on a Dictionary:
print("DICTIONARY METHODS".center(50, "+"))
[print(x) for x in dir(person) if not x.startswith("_")]  # (a list comprehension to print out all the Dictionary methods)
# clear()	    - Removes all the elements from the dictionary
# copy()	    - Returns a copy of the dictionary
# fromkeys()	- Returns a dictionary with the specified keys and value
# get()	        - Returns the value of the specified key
# items()	    - Returns a list containing a tuple for each key value pair
# keys()	    - Returns a list containing the dictionary's keys
# pop()	        - Removes the element with the specified key
# popitem()	    - Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - Updates the dictionary with the specified key-value pairs
# values()	    - Returns a list of all the values in the dictionary

print("SETS".center(50, "+"))  # Output separator
# ---Sets
# ----Set / set: x = {"one", "two", "three", "three"}
# ----Frozen Set / frozenset: frozenset({"one", "two", "three", "three"})

print("BOOLEAN VALUES".center(50, "+"))  # Output separator
# ---Boolean
# ----Boolean / bool: x = True
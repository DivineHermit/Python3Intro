"""
    Python3 Introduction
    More Data Types: Dictionaries, Sets and Boolean Values.
    Written by: Dominic Lee
    Date: 30-11-2023
"""
print("DICTIONARIES".center(50, "+"))  # Output separator
# Dictionaries are Lists consisting of Key & Value pairs, while Lists can use an index to access a value,
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
print("Key: name / Value:", person['name'])

# We can get all the Keys or all the Values with the following methods:
print("Keys".ljust(7), "=", person.keys())
print("Values".ljust(7), "=", person.values())

# Since we lost Bob while covering Lists lets update his status:
person["status"] = "M.I.A."
print("Bobs status is:", person.get("status"))

# Lets take a look at the methods available on a Dictionary:
print("\nDICTIONARY METHODS:")
[print(x) for x in dir(person) if not x.startswith("_")]  # (a List comprehension to print out all the Dictionary methods)
# clear()	    - Removes all the elements from the dictionary
# copy()	    - Returns a copy of the dictionary
# fromkeys()	- Returns a dictionary with the specified keys and value
# get()	        - Returns the value of the specified key
# items()	    - Returns a List containing a tuple for each key value pair
# keys()	    - Returns a List containing the dictionary's keys
# pop()	        - Removes the element with the specified key
# popitem()	    - Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - Updates the dictionary with the specified key-value pairs
# values()	    - Returns a List of all the values in the dictionary

print("SETS".center(50, "+"))  # Output separator
# Sets look a lot like Lists made with curly brackets '{}'.
numbers = {"one", "two", "three", "three", "four"}
# As you can see creating a Set is easy, but if we print out the above Set you'll see it works differently to a List.
print(numbers)
# Sets are 'unordered', do not alow duplicate items and do not alow items inside them to be changed, though you can add or remove items.
# Unordered means that we can not use an index or key to access items as we have done previously,
# as the order of the items can change every time you use them, the above print statement probably displayed something like:
# {'two', 'four', 'one', 'three'} even though we put the numbers in order when we created the Set.

# You will also have noticed when we made the Set we included two(2) instances of 'three', but only one(1) is actually included in the Set.

# Since we can not access the items direct, they are unchangeable, indexing like 'numbers[1]' will trigger a TypeError.

print("\nSET METHODS:")
[print(x) for x in dir(numbers) if not x.startswith("_")]  # (a List comprehension to print out all the Set methods)
# Method summery from: https://www.w3schools.com/python/python_sets_methods.asp
# add()	                        - Adds an element to the set
# clear()	                    - Removes all the elements from the set
# copy()	                    - Returns a copy of the set
# difference()	                - Returns a set containing the difference between two or more sets
# difference_update()	        - Removes the items in this set that are also included in another, specified set
# discard()	                    - Remove the specified item
# intersection()	            - Returns a set, that is the intersection of two other sets
# intersection_update()	        - Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                - Returns whether two sets have a intersection or not
# issubset()	                - Returns whether another set contains this set or not
# issuperset()	                - Returns whether this set contains another set or not
# pop()	                        - Removes an element from the set
# remove()	                    - Removes the specified element
# symmetric_difference()        - Returns a set with the symmetric differences of two sets
# symmetric_difference_update() - Inserts the symmetric differences from this set and another
# union()	                    - Return a set containing the union of sets
# update()	                    - Update the set with the union of this set and others

print("BOOLEAN VALUES".center(50, "+"))  # Output separator
# A Boolean is a simple binary choice of True or False, occasionally 1 or 0.
# There are many methods, some we've looked at previously, start with 'is' like the string methods: 
# isnumeric(), isspace(), istitle(), isupper()
# These methods all return a True or False value and can be used to check expressions, create logic and control the flow of a program.
# Lets take a look at an example:
your_age = input("Enter your age: ")  # (any number will do)
print(f"You entered '{your_age}' is this a numerical value?: {your_age.isnumeric()}")
# You can see in the f-string above we call 'isnumeric()' on the users input and even though it's a string 'isnumeric()' can detect
# the numbers and returns 'True'. So we can use it in an 'If' statement to control what gets printed:
if your_age.isnumeric():
    # if you enter something that can be converted to a number, like 21, this message will be printed.
    print("You entered a number, YAY!")
else:
    # if 'isnumeric()' can't determine a numerical value, this message is printed instead.
    print("That may not be a number!")


"""
Q01) Create a dictionary to represent a person. (Hint: think of the field in your phones contacts app. Use None for the values.)
A01)

Q02) Now use your above dictionary to create two representations of a person.
     Use the dictionary methods or square bracket method to add/alter values.
    (Hint: Don't use a real info, try picking a fictional character.)
A02)

Q03) Dictionaries and Set both use curly brackets but describe the differences between the two data types.
A03) 

Q04) 
A04) 
"""
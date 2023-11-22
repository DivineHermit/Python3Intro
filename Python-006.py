"""
    Python3 Introduction
    More Data Types: Sequences/Iterables - Lists, Tuples and Ranges.
    Written by: Dominic Lee
    Date: 
"""
print("SEQUENCES & ITERABLES".center(50, "+"))  # Output separator
print("LISTS & LIST METHODS:")
# A list is a way of storing multiple bit of data in one(1) variable, they are created by using square brackets '[]' and
# separating the data with a comma ','. Lets create a list of UK cities:
cities = ["London", "Birmingham", "Manchester", "Bristol", "Leeds", "Nottingham",
          "Aberdeen", "Cambridge", "Leicester", "Oxford", "Coventry", "York", "Plymouth"]
# Now we have a list stored in the 'cities' variable, lets print off all the methods we can use
[print(x) for x in dir(cities) if not x.startswith("_")]  # (a list comprehension to print out all the list methods)

# append()	-   Adds an element at the end of the list
# clear()	-   Removes all the elements from the list
# copy()	-   Returns a copy of the list
# count()	-   Returns the number of elements with the specified value
# extend()	-   Add the elements of a list (or any iterable), to the end of the current list
# index()	-   Returns the index of the first element with the specified value
# insert()	-   Adds an element at the specified position
# pop()	    -   Removes the element at the specified position
# remove()	-   Removes the item with the specified value
# reverse()	-   Reverses the order of the list
# sort()	-   Sorts the list

# As usual we can just print out the data in the list using the 'print' function:
print("\nCities list:")
print(cities)  # not the prettiest output, but we can see the list.
# We can access individual items in a list using indexes and slicing like we did with strings:
print("\nFirst list item:", cities[0])  # this will get the first item in the list (this should be London).

# We can sort the list by calling the 'sort()' method on our 'cities' list and then printing it out again:
cities.sort()  # the sort function will alter the order of the items inside the list, so the indexes will be different after:
print("First list item:", cities[0])  # the first item should now be Aberdeen.

# Slicing a list is just like slicing a string, using the [::] format:
print("\nFirst three cities:")
print(cities[:3])  # slice the first three(3) items, remember the three(3) is the last index and is not included in the slice.

# We can add items to a list with the 'append()' method:
print("\nThe return of Bob!")
cities.append("Bob")
print(cities)  # We now have a list of cities and Bob (he gets everywhere!)
# No offense to Bob, but he really doesn't belong in a list of cities, lets replace him with a different city, there are a few ways we can do this.
# Since 'Bob' is the last item in the list we could use a negative index like: cities[-1] = "Derby"
# but this is risky as we don't know for sure if the list order has changed since Bob was added, lets sort the list and see how to safely replace bob.
print("\nSorted cities list, now Bob is lost!")
cities.sort()  # Now Bob is somewhere in the list, but where?
print(cities)

# We can use the 'index()' method to get Bobs index and replace him with the name of a city:
print("\nBobs index is:", cities.index("Bob"))
# now we have the index, lets replace Bob, poor Bob.
bobs_index = cities.index("Bob")  # save the index into a variable to use in the next bit of code 
cities[bobs_index] = "Derby"
# Since index returns an integer we can place it directly into the slice and it would save a line of code, but this is bad practice and not Pythonic code.
print(cities)  # Bob is gone now, bye bye Bob!

print("\nTUPLES:")  # Output separator
# ----Tuple / tuple: x = (1, 2, 3)
# ----Range / range: x = range(6)

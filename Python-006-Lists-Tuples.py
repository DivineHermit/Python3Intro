"""
    Python3 Introduction
    More Data Types: Sequences/Iterables - Lists & Tuples
    Written by: Dominic Lee
    Date: 23/11/2023
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
# but this is risky as we don't know for sure if the list order has changed since Bob was added, lets sort the list and see how to safely replace Bob.
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
# Tuples are very similar to lists, the first difference is they are created with round brackets '()'. Lets make a tuple of country names:
countries = ("England", "America", "France", "Bob", "Spain", "Germany", "Italy", "England")  # We now have our tuple, something seems odd, oh well.
print("\nA tuple of countries:")
print(countries)

# Lets see what methods we can use on tuples:
print("\nTuple methods:")
[print(x) for x in dir(countries) if not x.startswith("_")]  # (a list comprehension to print out all the tuple methods)
# As you can see, there aren't that many things we can do to our tuple. 

# The count method will return an integer 
print(f"\nThere are {countries.count("England")} instances of 'England' in the tuple.")
print(f"There is {countries.count("Bob")} instance of 'Bob' in the tuple.")  # Wait a minute... BOB!

# The index method will return the index location of the given item, lets locate Bob:
print(f"Bob's index is {countries.index("Bob")}")

# Tuples are immutable like strings, meaning once created tuples can NOT be added to or have items removed from them.
# This means Bob is stuck somewhere between France and Spain forever, kinda.

# If you need to change a tuple you have to create an entirely new tuple with the data you want.
# The easiest way is to turn the tuple into a list, add/remove the items and then turn the updated list into a tuple.
print("\nTurn the tuple into a list:")
countries = list(countries)  # we can use the list keyword/function to convert our tuple to a list
print(f"'countries' is now a list ({type(countries)})", countries)
countries.remove("Bob")  # Poor Bob, he's been kicked out.
# Now we can turn the list back into a tuple, with another keyword/function:
countries = tuple(countries)  # countries is now a tuple once again.
print(countries)  # Back to where we started, except for Bob, poor Bob.

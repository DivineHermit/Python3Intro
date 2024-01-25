"""
    Python3 Introduction
    Control and Flow: 'for' and 'while' loops.
    Written by: Dominic Lee
    Date: 3-12-2023
"""
print("WHILE LOOPS".center(50, "+"))  # Output separator
# While Loops will repeat a section of code over and over and over and over... until a specified condition is met.
count = 0  # create a counter variable to keep track of how many loops we've done
while count <= 10:  # start a while loop with the 'while' keyword and specify the condition to check, 'count' is less then or equal to 10,
    print(count)  # print out the current value of 'count'
    count += 1  # increase 'count' by 1 (see section 005-Operators if you need a reminder)
    # if 'count' is 10 or less the code will go back to line 9 and loop
print("First loop done!")  # This, and following lines, of code is only ran when 'count' has a value of 11 and the loop finishes. 

# Lets take a look at how to stop a loop early:

while count <= 1_000_000_000:  # loop one(1) BILLION time, ooh thats a lot of loops, I'm dizzy just thinking about it!
    if count == 101:  # an if statements checks the current value of 'count' and triggers when 'count' is 101
        break  # the keyword 'break' will stop the loop regardless of the original condition, in this case: count <= 1_000_000_000
    print(count)  # just print out count till the loop stops, so we can see what is happening.
    count += 1  # make sure to increase 'count' each time we loop, or we'll get stuck in an infinite loop.
print("Second loop finished!")  # This and following lines only run when the second loop finishes.

# We can also you the boolean value True to create an infinite loop:
count = 0  # reset the counter.
while True:
    # Since True is always true, this loop will run forever.
    if count > 10: break  # so we need to include a way to stop the loop, when count gets to eleven(11) this will break the loop.
    print(count)  # print out the counter so we can see what is happening.
    count += 1  # increase the count each time through the loop.

print("FOR LOOPS".center(50, "+"))  # Output separator
print("Range example:")
# A 'for' loop is used to iterate over an iterable... thats programmer speak for a list or range of values/data.
for x in range(11):  # each time this loop runs the next value in the range will get saved to 'x'
    print("x =", x)

print("List:")
fruits = ["Apple", "Orange", "Grape", "Mellon", "Banana"]
for fruit in fruits:
    print("fruit =", fruit)

# For loops are generally faster than While loops but you should use built in functions if available as they are much faster.
# Example, instead of looping over a list of numbers to add them all together, use the built in sum() function.

print("\nPlaceholder Variables:")  # Output separator
# You can use an '_' as a placeholder for unused data. Below gets the Key and Value from a dictionary but we ignore the key and only print the value.
example_dict = {1:"one", 2:"two", 3:"three"}
for _, val in example_dict.items():
    print(val)

# A better way of doing the above is to just get the values from the dictionary:
for value in example_dict.values():
    print(value)


"""
Q01)
A01)

Q02)
A02)

Q03) Create a for loop to iterate over the list and print out each item 
A03)
numbers = ["one", "two", "three", "four", "five"]

Q04)
A04)
"""

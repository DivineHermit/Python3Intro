"""
    Python3 Introduction
    Variables and assignment.
    Written by: Dominic Lee
    Date: 02/11/2023
"""
print("VARIABLES".center(50, "+"))  # Output separator
# There are some rules when it comes to naming variables
# variable names can NOT start with a number e.g. 1st_name = "John"
# they can only use letters, numbers or the underscore '_' e.g. var_1, v2, VAR
# they are case sensitive e.g. var, Var & VAR are three separate variables
# variables in all capitols e.g. ONE = 1 are considered constants and the data inside them should not be altered while running

# There are three common style of writing variable names
# camelCase - you see this style a lot in C and Java languages
yourVariableNameHere = "Camel Case"
# PascalCase
YourVariableNameHere = "Pascal Case"
# snake_case - this is the preferred style for Python as it is easy to read
your_variable_name_here = "Snake Case"

# Variables are containers for data, a part of the the computers memory where we can store something 
# a variable should be named descriptively so it is easy to tell what it contains, and is written with the following format:
# 'name of the variable' = 'data to place inside the variable'
# for example:
name = "Bob"

# Python creates variable dynamically, just by assigning some data to the variable
# in the above example 'name' becomes a variable containing the string "Bob"
# Note: we'll cover strings and data types later.

# The above example is a 'hard coded' variable.
# We chose the name of the variable, 'name', and gave it a specific bit of data, "Bob"
# We'll be doing this a lot but it is worth noting that we wont always know what the data is, just what it's supposed to be
# so when writing code in later classes, the code can be somewhat abstract and a little removed the task you are trying to accomplish
# this can be confusing at first but get easier with practice and repetition.

# It is usually best practice to do one(1) variable assignment per line:
age = 32
pet = "Dog"

# but you can do multiple variables on a single line:
a, b, c = 1, 2, 3
# 'a' would contain the number 1, 'b' would contain 2 and can you guess what 'c' contains?
print(a,b,c)  # we can print the variables to see there contents.

# Variables also have a 'scope' this is an area of the code that has access to the variable
# or what part of the code is aware that the variable exists.
# The variables created above are considered to be in the 'global' scope and could be easily used anywhere in this file.

# You can also make large integers easier to read by using underscores:
large_int = 1_000_000_000

# VARIABLE SCOPE #
# ============== #
print("VARIABLE SCOPE".center(50, "+"))  # Output separator
# However there are other types of 'scope' like 'if' statements, while & for loops and functions, we'll go into each of these in detail later,
# but for now here is an example of a variable inside a function:
def example_function():
    # The indented code of a function is its own scope
    name = "Dorothy"
    # print the above variable
    print(name)
    # The scope of the function stops here.

# we'll 'call', or activate the above function and see what out put we get
example_function()
# and now we'll print the 'name' variable and see what has changed:
print(name)
# as you can see when we created the 'name' variable inside the function it didn't override the original variable
# created at the beginning of this script.

# UNPACKING #
# ========= #
print("UNPACKING".center(50, "+"))  # Output separator
# Finally, you can unpack items from some other data types, like lists, sets or tuples, into individual variables
# we'll cover tuples in more detail later but below is a tuple with five(5) pieces of data,
# creating a tuple is sometimes know as 'packing a tuple'.
colours = ("red", "green", "blue", "white", "black")

# Unpacking allows us to place one(1) item, from a tuple, into one(1) variable
# lets place the first three(3) items into their own variables, and to avoid errors we'll dump the last two items into their own variable
r, g, b, *o = colours

print(r)  # the 'r' variable now contains 'red'
print(g)  # the 'g' variable now contains 'green'
print(b)  # the 'b' variable now contains 'blue'
print(o)  # and the 'o' variable contains a list of any left over data from the tuple, in this case the 'white' & 'black' items

# VARIABLE QUESTIONS:
"""
Q01) Give three examples of variable assignment.
A01) 

Q02) True or false: You can assign multiple variables on a single line.
A02) 

Q03) Are the variable 'name' and 'Name' the same?
A03) 

Q04) Give an example of the same variable in Camel case, Pascal case and Snake case.
A04) 

Q05) If you were going to store some data about a person, give examples of good variable names and datatypes to do so.
A05)
"""

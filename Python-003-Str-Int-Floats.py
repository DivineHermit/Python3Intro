"""
    Python3 Introduction
    Data types: Strings, Integers and Floating Point Numbers.
    Written by: Dominic Lee
    Date: 09/11/2023
"""
# CASTING: str() / int() / float()
# ============================== #
print("CASTING".center(50, "+"))  # Output separator
# You have learned how to assign variables with different types of data.
# We'll take a closer look at String, Integers and Floats, but first we'll look at assigning specific data types to variables.

# Let's welcome 'Bob' back, and save him into a variable again:
name = "Bob"
# Python knowns anything inside speech marks is a string, we can check this by printing out the type of the 'name' variable:
print(type(name))
# The output should be similar to "class 'str'".
# This means we can use the 'name' variable just like a string, using concatenation, methods and formatting.
# We'll cover all of those a little later.

# But if we want to be sure of the data type being assigned we can use casting.
# So lets update the name variable and be a little more specific:
name = str("Bob")
# This time we used the keyword 'str()', this is actually a function just like the the 'print()' function we've been using.
age = int("32")
# Here we have given the string of "32" to the int() function and saved it to a new variable called 'age'.
# But by specifically using the int() function the data type of age is an integer, a round/solid number.
# Lets check and see:
print("The 'name' variable contains:", name, "and has the" , type(name), "datatype.")
print("The 'age' variable contains:", age, "and has the" , type(age), "datatype.")

# So by using certain functions/keywords we can make sure the data we are assigning to a variable is the correct data type.
# However, if you try assigning an integer as follows, you'll get an error: num = int("A")
# The error that you get will look something like:
# ValueError: invalid literal for int() with base 10: 'A'
# This means that the string value that we passed to the int() function couldn't be interpreted as a numerical value.

# USER INPUT: x = input("Enter your name: ")
# ======================================== #
print("USER INPUT".center(50, "+"))  # Output separator
# Casting can help control the datatype people input into our programs, lets get the users name:
name = input("What is your name? >>> ")
print(f"You entered '{name}'. \nData type is: {type(name)}")
# After creating a variable we ask the user for their name using Pythons 'input' function.
# The string given to the input function will be displayed similarly to the 'print' function, however the program will wait for the users input
# and confirmation by pressing the Enter/Return key. The input is then stored in the 'name' variable.
# You may have noticed that we haven't used any casting to say the datatype should be a string, this is because 'input' always returns a string.
# So what if we want a numerical input for the users age?
age = input("What is your age? >>> ")
print(f"You entered '{age}'. \nData type is: {type(age)}")
# This would allow for user input, but we still get a string. But we can use casting to get a numerical value
age = int(input("Enter your age again, please. >>> "))
print(f"You entered '{age}'. \nData type is: {type(age)}")
# So what happened? for the 'name' variable our input went directly from the 'input' function into the 'name' variable.
# But this time when we confirmed our input it got passed into the 'int' function that tries to turn it into a integer and then it gets put
# into the 'age' variable. Do note however this on;y works if the 'int' function can turn the input into an integer:
# entering '32' can be turned into the integer 32, while entering 'thirty two' will raise a ValueError and crash the program, unless you write code to handle that.

# TYPE HINTING: x: str = "bob"
# ========================== #
print("TYPE HINTING".center(50, "+"))  # Output separator
# Type hinting is something we can add to our code to tell other, and our future selves, what our code is expecting for values or input.
year: int = 2023
# Above we create a variable called 'year', we use Stephen's favorite ':' character, and the 'int' keyword.
# this tells us we are expecting an integer to be placed in side the 'year' variable.
print(year, type(year))

# However Python doesn't enforce type hinting, lets reassign the 'year' variable with a string while still hinting it should be a integer:
year: int = "2023"
print(year, type(year))
# 'year' is now a string variable instead of in integer, so if your code needs a specific datatype you'll have to code in checks before
# allowing your program to continue running. 

# Type hinting can be useful as more powerful IDE's can detect the type hinting and offer guidance when using other peoples code.

# STRING, INTEGER & FLOAT QUESTIONS:
"""
Q01) Give an example of string assignment using casting.
A01)

Q02) What is the datatype for the 'x' variable in the following code:
     x = input("Enter your name: ") # user enters 6.9
A02) 

Q03) True or False: Type Hinting forces the datatype to match the hinting.
A03) 

Q04) Give an example of integer assignment using casting.
A04)

Q05) How could you change 'x = "42"' so the 'x' variable contains an Integer instead of a String?
A05) 

Q06) What is the value of x in the following code: x = int(3.1415)
A06)

Q07) Give an example of float assignment using casting.
A07)

You could also have a go at Project-002-Input.py
"""

"""
    Python3 Introduction
    Functions.
    Written by: Dominic Lee
    Date: 
"""
print("FUNCTIONS".center(50, "+"))  # Output separator
# A common principle in programming is D.R.Y. or 'Don't Repeat Yourself'.
# if you are using the same bit of code several times in a scrip or project and need to change something you'll
# have to change it at multiple places in the script and this increases the change of errors and bugs.

# So one way of not repeating the same code is to create a function, a bit of code that can be referred to as many times as needed.
# To create a function we define it using the 'def' keyword followed by the name of the function and finished with parenthesis and a ':'

def greeting():
    print("Hello, Hi, Greetings, Welcome!")

# If we run this script now, nothing will be displayed as we haven't 'called' the function,
# 'calling' is the term to activate the function and run that block of code.
# Calling the function is as simple as typing out the functions name with the parentheses:
greeting()

# Functions can be given data through the use of arguments and keyword arguments, sometimes collectively called parameters.
# Let's update the 'greeting' function to take in a name as an argument and print out a personal greetings:
def greet_person(name):
    print(f"Greetings {name}")

# We can now call our function and give it a name to use in the greeting.
greet_person("Dominic")

print("\nRETURN VALUES:")
# The last two function examples have been the absolute minimum needed to create working functions, but we can include previously covered
# topics Doc-Strings and Type Hinting to make our code more readable and user friendly:
def greet(name: str) -> None:
    """
    Print out a personalized greeting using the given name.

    Parameters:
        name - A string containing the name to greet.

    Return:
        None - Returns None
    """
    print(f"Hi {name}.")
    return None
# This may look much more complicated at first but supplies us with all the information on what the function expects as input,
# the docstring describes the function, parameters and what the function returns.

# A function ALWAYS returns something, even the first two(2) examples return something, but Python let us get away with not specifying 'return'
# and did it for us in the background.
# If no return value is specified, the function will return a 'None' value, basically a null/placeholder value.

# Lets see how we can use return values, combining it with variable assignment:
def add(Val1, Val2):
    """ Add Val1 and Val2 together and return the result. """
    return Val1+Val2
# The above example take two(2) arguments/parameters and combines them, this can have a few outcomes based on what data is given to hte function:
print(add(1,1))  # By using a return value, we can pass our function output to other function, as an argument, like the built in print function.
print(add("Hello ", "World!"))  # since the '+' operator works on strings, our function will also work if we give it strings as arguments.

print("\nCAPTURING OUTPUT:")
# Now that our functions have a return value we can capture the output and store it in a variable:
answer = add(5, 5)  # 5+5 is 10 so answer with contain 10, lets print it out and see:
print("add(5, 5) returned a value of", answer)

# Some best practices when defining a function are:
# Descriptive names: Using snake case the functions name should describe what it does.
# Do one thing:      A function should focus on doing just one thing, if you're writing a long function it may need breaking down into smaller functions.
# Limited arguments: Try to keep your argument/parameter use to as few as possible, aim for four(4) or less.

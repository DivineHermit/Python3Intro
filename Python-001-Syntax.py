"""
    Python3 Introduction
    Basic syntax and comments.
    Written by: Dominic Lee
    Date: 02/11/2023
"""
print("SYNTAX".center(50, "+"))  # Output separator
# Any line that stats with '#' is a comment and will be ignored when you run your code.
# print("This will not be shown!")

# Comments allow us to leave useful bits of info about the code we write
# as future you will probably not know what current you was thinking!

# Comments are usually written on the line directly above the code that the comment is about e.g.
# Print out the mandatory new Python programmers greeting:
print("Hello World!")

# They can also be on the same line as the code e.g.
print("There is a comment after this code!")  # This is an in-line comment, two spaces separate the code and the '#'

# It is best practice to avoid writing long lines of code,
# limiting them to seventy-nine(79) characters,
# or adding in-line comments that roll of the edge of the screen
# many IDEs will complain if your lines go over one-hundred(100) characters

print("INDENTATION".center(50, "+"))  # Output separator
# Python uses indentation, or whitespace, to structure itself
# to indent code you need at least one(1) space, but four(4) is considered best practice
if True:  # This is an 'IF' statement, the code inside only runs if the condition is met.
    # True is always true or one(1), so the following code will run.
    print("Have fun!")

# An 'IF' statement can have multiple parts, the simplest is an IF/ELSE statement
# if the condition is not met, then the code in the 'else' section is ran
if False:
    # False is always false or zero(0) so this section of code will not run
    print("This will never print!")
else:
    # No other conditions were set so this code is ran
    print("I am not false!")

# QUESTIONS:
"""
Q01) Give at least two examples of printing data to the screen?
A01) 

Q02) How much indentation is needed when writing IF statements, for loops and while loops?
A02) 

Q03) What is the structure of an IF and an IF/ELSE statements?
A03)

Q04) What symbol is used to start a comment in Python?
A04) 

Q05) How is a comment different from a line of Python code?
A05) 

Q06) Where is the best place to put a comment?
A06)  
"""
"""
    Python3 Introduction
    Functions.
    Written by: Dominic Lee
    Date: 
"""
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

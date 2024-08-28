"""
    Python3 Introduction
    Operators, Integers, Floats and Random Numbers.
    Written by: Dominic Lee
    Date: 18/11/2023
    NOTE: I HAVE USED ';' TO ALLOW MULTIPLE BITS OF CODE ON ONE LINE,
    THIS IS NOT BEST PRACTICE AND JUST TO COMPACT THE CODE TO EACH SECTION.
    RUN THE SCRIPT TO SEE THE OUTPUT EASILY.
"""
# OPERATORS #
# ========= #
# Operators are used in a variety of ways, assignment, comparison, math, logic and more.

# ASSIGNMENT:
print("ASSIGNMENT OPERATORS".center(50, "+"))  # Output separator
# The basic assignment you're already familiar with.
#  = 	x = 5 	    x = 5
x = 5; print("x = 5 | x now hold the value of:", x)

# += 	x += 3 	    x = x + 3
# This will add to the value already stored in the variable, so if x = 5 then x += 3 x would now hold the value of 8
x = 5; x += 3; print("x = 5 | x += 3  | x now hold the value of:", x)

# -= 	x -= 3 	    x = x - 3
# This will subtract from the value already stored in the variable, so if x = 5 then x -= 3 x would now hold the value of 2
x = 5; x -= 3; print("x = 5 | x -= 3  | x now hold the value of:", x)

# *= 	x *= 3 	    x = x * 3
# This will multiply the value already stored in the variable, so if x = 5 then x *= 3 x would now hold the value of 15
x = 5; x *= 3; print("x = 5 | x *= 3  | x now hold the value of:", x)

# /= 	x /= 3 	    x = x / 3
# This will divide the value already stored in the variable, so if x = 5 then x /= 3 x would now hold the value of 1.6666666666666667
x = 5; x /= 3; print("x = 5 | x /= 3  | x now hold the value of:", x)

# %= 	x %= 3 	    x = x % 3
# The modulo operator saves the remainder from a division, so if x = 5 then x %= 3 x would now hold the value of 2
x = 5; x %= 3; print("x = 5 | x %= 3  | x now hold the value of:", x)

# //= 	x //= 3 	x = x // 3  
# Floor/Integer division will give the rounded down value from the calculation, x = 5 then x //= 3 x would now hold the value 1
x = 5; x //= 3; print("x = 5 | x //= 3 | x now hold the value of:", x)

# **= 	x **= 3 	x = x ** 3
# The power operator will multiply the value of x by itself the given amount of times, x = 5 then x **= 3 x will now hold 125
x = 5; x **= 3; print("x = 5 | x **= 3 | x now hold the value of:", x)

# COMPARISON:
print("COMPARISON OPERATORS".center(50, "+"))  # Output separator
# ==    Equal                       (x == y)
# You're already familiar with '=' for assigning data to a variable, but you can also use '==' for comparison.
a = 5; b = 5; print(f"Are 'a={a}' and 'b={b}' equal? :", a == b)

# !=    Not equal                   (x != y)
# We can flip some comparison logic by using an exclamation '!' mark, this could be used in an IF statement to ignore equal values.
a = 5; b = 10; print(f"Are 'a={a}' and 'b={b}' NOT equal? :", a != b)

# >     Greater than                (x > y)
# This checks if the left/first value is higher then the right/second value.
# The left/first value MUST be higher for this comparison to be true.
a = 5; b = 5; print(f"Is 'a={a}' greater then 'b={b}'? :", a > b)

# <     Less than                   (x < y)
# This checks if the left/first value is lower than the right/second vale.
# The left/first value MUST be lower for this comparison to be true.
a = 5; b = 10; print(f"Is 'a={a}' less then 'b={b}'? :", a < b)

# >=    Greater than or equal to    (x >= y)
# The left/first value can be higher or equal to the right/second value for the comparison to be true.
a = 5; b = 5; print(f"Is 'a={a}' greater then or equal to 'b={b}'? :", a >= b)

# <=    Less than or equal to       (x <= y)
# The left/first value can be lower or equal to the right/second value for the comparison to be true.
a = 5; b = 5; print(f"Is 'a={a}' less then or equal 'b={b}'? :", a <= b)

# RANDOM NUMBERS #
# ============== #
print("RANDOM NUMBERS".center(50, "+"))  # Output separator
# Python doesn't have a built-in way of generating a random number so we'll need to look to the standard library.
# The standard library is a bunch of code modules holding extra functionality that comes with Python but are not directly access,
# like the 'print', 'input' or datatype functions we've used so far.
# We'll use the 'random' module, which hold several new functions, to generate some random numbers, first we need to import the module:
import random  # side note: imports are supposed to go at the top of the script, right after the Doc-String
# from this point on we have access to the new functions lets get a random integer
print("The 'randint' method chose:", random.randint(0, 101), "Run the script again and see if it chooses something different.")
# above we access the random module and use the 'randint' function to get a random number between 0 and 100, as 101 is not included in the range.

# MATH OPERATORS #
# ============== #
print("MATH OPERATORS".center(50, "+"))  # Output separator
# Lets start with the basic maths operators, we'll even use random numbers so the output changes each time the script is ran. 
val1, val2 = random.randint(1, 101), random.randint(1,101)
# Addition:
# the versatile '+' is used for addition.
print(f"Addition:\n{val1}+{val2} =", val1 + val2)
# Subtraction:
# as you have probably guessed, we use '-' for subtraction.
print(f"Subtraction:\n{val1}-{val2} =", val1 - val2)
# Multiply:
# an asterisk '*' is used for multiplication
print(f"Multiplication:\n{val1}*{val2} =", val1 * val2)
# Division:
# a single forward slash '/' is used to divide the first value between the second value.
print(f"Division:\n{val1}/{val2} =", val1 / val2)
# Floor division:
# This divides the first value by the second and rounds down to the nearest whole integer.
print(f"Floor Division:\n{val1}//{val2} =", val1 // val2)
# Power:
# multiply the first value by itself a given number (second value) of times.
print(f"Power:\n{val1}**{val2} =", val1 ** val2, f"\n({ 'x'.join([str(val1) for x in range(val2)])})")
# Note: the list comprehension above is used to print out an alternative visual representation of the power calculation.

# OPERATOR QUESTIONS:
"""
Q01)
A01)

Q02)
A02)

Q03)
A03)

Q04)
A04)

Q05)
A05)
"""
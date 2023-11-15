"""
    Python3 Introduction
    Operators, Integers, Floats and Random Numbers.
    Written by: Dominic Lee
    Date: 
"""
# OPERATORS #
# ========= #
print("OPERATORS".center(50, "+"))  # Output separator
# Operators are used in a variety of way, assignment, comparison, math, logic and more.

# ASSIGNMENT:
print("ASSIGNMENT OPERATORS:")
# The basic assignment you're already familiar with.
#  = 	x = 5 	    x = 5
x = 5; print("x = 5 | x now hold the value of:", x)
# This will add to the value already stored in the variable, so if x = 5 then x += 3 x would now hold the value of 8
# += 	x += 3 	    x = x + 3
x = 5; x += 3; print("x = 5 | x += 3  | x now hold the value of:", x)
# This will subtract from the value already stored in the variable, so if x = 5 then x -= 3 x would now hold the value of 2
# -= 	x -= 3 	    x = x - 3
x = 5; x -= 3; print("x = 5 | x -= 3  | x now hold the value of:", x)
# This will multiply the value already stored in the variable, so if x = 5 then x *= 3 x would now hold the value of 15
# *= 	x *= 3 	    x = x * 3
x = 5; x *= 3; print("x = 5 | x *= 3  | x now hold the value of:", x)
# This will divide the value already stored in the variable, so if x = 5 then x /= 3 x would now hold the value of 1.6666666666666667
# /= 	x /= 3 	    x = x / 3
x = 5; x /= 3; print("x = 5 | x /= 3  | x now hold the value of:", x)
# The modulo operator saves the remainder from a division, so if x = 5 then x %= 3 x would now hold the value of 2
# %= 	x %= 3 	    x = x % 3
x = 5; x %= 3; print("x = 5 | x %= 3  | x now hold the value of:", x)
# Floor/Integer division will give the rounded down value from the calculation, x = 5 then x //= 3 x would now hold the value 1
# //= 	x //= 3 	x = x // 3  
x = 5; x //= 3; print("x = 5 | x //= 3 | x now hold the value of:", x)
# The power operator will multiply the value of x by itself the given amount of times, x = 5 then x **= 3 x will now hold 125
# **= 	x **= 3 	x = x ** 3
x = 5; x **= 3; print("x = 5 | x **= 3 | x now hold the value of:", x)

# COMPARISON:
print("\n\nCOMPARISON OPERATORS:")
# ==    Equal                       x == y
# !=    Not equal                   x != y
# >     Greater than                x > y
# <     Less than                   x < y
# >=    Greater than or equal to    x >= y
# <=    Less than or equal to       x <= y

# You're already familiar with '=' for assigning data to a variable, but you can also use '==' for comparison.
a = 5
b = 5
print("Are 'a' and 'b' equal? :", a == b)



# ---Numeric
# ----Integer / int: x = 1
# ----Floating Point / float: x = 1.0

# ----Random Numbers: import random
# Modules & Packages in Python

# 1. Importing entire module
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# 2. Importing specific function
from math import factorial
print("Factorial of 5:", factorial(5))

# 3. Importing with alias
import math as m
print("Power 2^3:", m.pow(2, 3))

# 4. Random module
import random
print("Random integer (1-10):", random.randint(1, 10))
print("Random fruit:", random.choice(["apple", "banana", "cherry"]))

# 5. Importing from custom module
# Suppose we have a file helpers.py with a greet() function
# helpers.py:
# def greet(name):
#     return f"Hello, {name}!"

# In this file:
# import helpers
# print(helpers.greet("Rakib"))

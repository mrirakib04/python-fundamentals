# Functions in Python

# Defining a simple function
def greet():
    print("Hello, welcome to Python functions!")

greet()


# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Rakib")


# Function with return values
def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)


# Function with default arguments
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

introduce("Rakib")          # uses default age = 18
introduce("Rakib", 20)      # overrides default


# Lambda functions (small anonymous functions)
square = lambda x: x * x
print("Square of 5:", square(5))

add_numbers = lambda a, b: a + b
print("Lambda Sum:", add_numbers(3, 4))

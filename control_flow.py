# Control Flow in Python

# Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# if-elif-else
marks = 75
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Nested conditions
num = 25
if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not positive.")

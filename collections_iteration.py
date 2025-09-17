# Collections & Iteration in Python

# 1. List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]   # square of each number
evens = [n for n in numbers if n % 2 == 0]  # filter even numbers

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", evens)


# 2. Dictionary Comprehensions
students = ["Rakib", "Rahim", "Karim"]
marks = [85, 90, 78]

student_dict = {name: mark for name, mark in zip(students, marks)}
print("Student Marks Dictionary:", student_dict)


# 3. Iterating with enumerate()
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# 4. Iterating with zip()
colors = ["red", "green", "blue"]
objects = ["pen", "book", "bottle"]

for color, obj in zip(colors, objects):
    print(f"{color} {obj}")

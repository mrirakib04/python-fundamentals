# Variables & Data Types

# Numbers
a = 10        # Integer
b = 3.14      # Float
c = 2 + 3j    # Complex number
print("Integer:", a)
print("Float:", b)
print("Complex:", c)

# Strings
name = "Rakib"
greeting = 'Hello'
print("Name:", name)
print("Greeting:", greeting)
print("Full Greeting:", greeting + " " + name)

# Booleans
is_active = True
is_admin = False
print("Active:", is_active)
print("Admin:", is_admin)

# Lists (mutable, ordered collection)
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits List:", fruits)
print("First fruit:", fruits[0])

# Tuples (immutable, ordered collection)
coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)
print("First coordinate:", coordinates[0])

# Sets (unordered, unique values)
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers Set:", unique_numbers)

# Dictionaries (key-value pairs)
person = {
    "name": "Rakib",
    "age": 18,
    "is_student": True
}
print("Dictionary:", person)
print("Name from dict:", person["name"])

# Type Conversion
x = "100"
y = int(x)       # String → Integer
z = float(x)     # String → Float
w = str(1234)    # Number → String

print("x:", x, type(x))
print("y:", y, type(y))
print("z:", z, type(z))
print("w:", w, type(w))

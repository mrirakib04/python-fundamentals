# Operators in Python

# Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)       # float division
print("Floor Division:", x // y)  # integer division
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Comparison Operators (returns True/False)
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Logical Operators
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Assignment Operators
z = 5
print("\nInitial z:", z)
z += 3   # z = z + 3
print("z after += 3:", z)
z -= 2   # z = z - 2
print("z after -= 2:", z)
z *= 4   # z = z * 4
print("z after *= 4:", z)
z /= 3   # z = z / 3
print("z after /= 3:", z)
z %= 2   # z = z % 2
print("z after %= 2:", z)

# Membership Operators
numbers = [1, 2, 3, 4, 5]
print("Is 3 in numbers?", 3 in numbers)
print("Is 10 not in numbers?", 10 not in numbers)

# Identity Operators
m = [1, 2, 3]
n = [1, 2, 3]
p = m

print("m is n:", m is n)       # False → different objects in memory
print("m == n:", m == n)       # True → values are equal
print("m is p:", m is p)       # True → same object reference

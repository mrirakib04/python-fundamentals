# Error Handling in Python

# Example 1: Basic try-except
try:
    num = int("abc")  # invalid conversion
except ValueError as e:
    print("Error occurred:", e)

# Example 2: Multiple except blocks
try:
    numbers = [1, 2, 3]
    print(numbers[5])  # Index out of range
except IndexError as e:
    print("Index error:", e)
except Exception as e:
    print("General error:", e)

# Example 3: try-except-finally
try:
    file = open("sample.txt", "w")
    file.write("Hello, World!")
    print(10 / 0)  # ZeroDivisionError
except ZeroDivisionError as e:
    print("Division error:", e)
finally:
    file.close()
    print("File closed (finally block executed).")

# Example 4: Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print("Custom exception:", e)

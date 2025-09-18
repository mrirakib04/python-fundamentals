# File Handling in Python

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a text file.\n")
    file.write("I am learning Python file handling.\n")

# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This line was appended later.\n")

# Reading again after append
with open("example.txt", "r") as file:
    print("Updated content:\n", file.read())

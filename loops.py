# Loops in Python

# for loop (iterating over a list)
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

# for loop with range()
for i in range(5):
    print("Number:", i)

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Loop control: break
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

# Loop control: continue
for i in range(5):
    if i == 2:
        print("Skipping", i)
        continue
    print("Value:", i)

# Loop control: pass
for i in range(3):
    if i == 1:
        pass  # placeholder, does nothing
    print("Index:", i)

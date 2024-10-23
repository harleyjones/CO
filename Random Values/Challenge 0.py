import random

# Generate and print a random decimal number
num = random.random()
print(num)

# Generate and print a random interger
num = random.randint(0, 100)
print(num)

# Generate and print a random interger that is a multiple of 5 between 0-100
num = random.randrange(0, 100, 5)
print(num)

# Generate and print a random item from a list
num = random.choice(["red", "blue", "black"])
print(num)
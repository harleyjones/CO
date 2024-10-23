import random

start = int(input("Enter a starting number:     "))
end = int(input("Enter a ending number:     "))

startdiv = (start % 2)

match startdiv:
    case 0:
        num = random.randrange(start, end, 2)
    case _:
        num = random.randrange(start + startdiv, end, 2)

print(num)
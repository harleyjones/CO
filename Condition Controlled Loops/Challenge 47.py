num = 0
num = int(input("Enter a number:    "))
total = num
question = "Y"
while question == "Y":
    num3 = int(input("Enter another number:    "))
    total = total + num3
    question = input("Would you like to enter another number:    ")
print(total)

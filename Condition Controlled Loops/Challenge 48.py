num = int(input("Enter a person's name:    "))
total = 1
question = "Y"
while question == "Y":
    num3 = int(input("Enter another number:    "))
    total = total + num3
    question = input("Would you like to enter another person's name:    ")
print(total)

def main():
    file = open('Names.txt', 'a')
    name = input('Enter a new name\n')
    file.write(f'{name}\n')
    file.close()

    file = open('Names.txt', 'r')
    print(file.read())
    file.close()

main()
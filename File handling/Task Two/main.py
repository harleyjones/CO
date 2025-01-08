def main():
    file = open('Countries.txt', 'r')
    print(file.read())
    file.close()

main()
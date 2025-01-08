def main():
    file = open('Names.txt', 'w')
    names = ['Harley', 'Alex', 'Jonjo', 'Glinda', 'Elphaba']

    for name in names:
        file.write(f'{name}\n')
    file.close()

main()
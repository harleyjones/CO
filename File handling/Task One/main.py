def main():
    file = open('Countries.txt', 'w')
    countries = ['Italy', 'Germany', 'Spain', 'England']

    for country in countries:
        file.write(f'{country}\n')
    file.close()

main()
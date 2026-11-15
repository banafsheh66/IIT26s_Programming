def main():
    print("Program starting.")

    firstName = input("Insert your first name: ")
    lastName = input("Insert your last name: ")
    fileName = input("Insert filename: ")

    file = open(fileName, 'w', encoding='utf-8')

    file.write(firstName + '\n')
    file.write(lastName + '\n')

    file.close()

    print("Program ending.")

main()   
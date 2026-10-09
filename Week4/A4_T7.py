
print("Program starting.")
print()

print("Check multiplicative persistence.")
Number = int(input("Insert an integer: "))

Steps = 0

while Number >= 10:
    Product = 1
    numbers = str(Number)

    for i in range(len(numbers)):
        Product = Product * int(numbers[i])

        if i == 0:
            print(numbers[i], end="")
        else:
            print(" * ", numbers[i], sep="", end="")

    print(" = ", Product, sep="")

    Number = Product
    Steps += 1

print("No more steps.")
print()
print(f"This program took {Steps} step(s)")
print()
print("Program ending.")

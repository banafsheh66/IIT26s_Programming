
print("Program starting.")

user_input = input("Insert comma separated integers: ")

values = user_input.split(",")
numbers_list = []

for value in values:
    value = value.strip()

    try:
        number = int(value)
        numbers_list.append(number)
    except ValueError:
        print(f"Invalid value: {value}")

if len(numbers_list) > 0:
    count = len(numbers_list)
    total = sum(numbers_list)

    if total % 2 == 0:
        result = "even"
    else:
        result = "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {result}")
else:
    print("No valid integers to analyze.")

print("Program ending.")

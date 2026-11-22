
def get_positive_integers():
    list_of_numbers = []
    print("Collect positive integers.")
    while True:
        
        num = int(input("Insert positive integer(negative stops):"))
        if num < 0:
            print("Stopped collecting positive integers.")
            break

        list_of_numbers.append(num)
    return list_of_numbers


def print_positive_integers(list_of_numbers):
    print("Displaying positive integers.")
    for i in range(len(list_of_numbers)):
        print(f"- Index {i} => Ordinal {i + 1} => Integer {list_of_numbers[i]}")
def main():
    print("Program starting.")
    list_of_numbers = get_positive_integers()

    print_positive_integers(list_of_numbers)

    print("Program ending.")

if __name__ == "__main__":
    main()    
 
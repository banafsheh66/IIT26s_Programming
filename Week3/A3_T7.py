print("Program starting.")
print("Testing decision structures.")
print("Insert an integer: ") 
number = int(input())

print("\nOptions:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
print("Your choice: ")
choice = input()
if choice == "1":
    if number >=400:
        number += 44
    elif number >= 200:
        number += 22
    elif number >= 100:
        number += 11
    print("Using one multi-branched decision structure.")    
    print("result is", number)


elif choice == "2":
    if number >= 400:
        number += 44
    if number >= 200:
        number += 22
    if number >= 100:
        number += 11
    print("Using multiple independent if-statements structure.")    
    print("result is", number)
    print("Using one multi-branched decision structure.")


elif choice == "0":
    print("Exiting...")
    print("Using one multi-branched decision structure.")

elif choice == "4":
    print("Unknown option.")

print("Program ending.")
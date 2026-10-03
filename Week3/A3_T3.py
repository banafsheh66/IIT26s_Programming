print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs")
name = input("Before the menu, please insert your name: ")
options = ["1 - Print welcome message", "0 - Exit"]
print("\nOptions:")
print("\n".join(options))
choice = input("Your choice: ")
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
  print("Unknown Option.")
elif choice == "0":
  print("Exiting...")
else:
  print("Your choice was 1.")
print("Program ending.")

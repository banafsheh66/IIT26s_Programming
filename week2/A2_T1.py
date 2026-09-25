
print("program starting")
Name = input("What is your name? ")
First_number = input("Enter a floating point number:")
First_number = float(First_number)
Second_number = input("Enter another floating point number:")
Second_number = float(Second_number)
print(f"{Name} you gave numbers {First_number} and {Second_number}")
Float_sum = First_number * Second_number
print(f"multiplying first and second number will result in product {round(Float_sum, 2)}")
print("program ending")

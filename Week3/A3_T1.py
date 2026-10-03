print("Program starting.")
print("Insert two integers.")
num1 = int(input("first integer: "))
num2 = int(input("second integer: "))  
print("Comparing inserted integers.")
if num1 == num2:
    print("Integers are the same")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")    

print("\nAdding integers together")
Z = num1 + num2
print(f"{num1} + {num2} = {Z}")
print("Checking the parity of the sum...")
if Z % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")
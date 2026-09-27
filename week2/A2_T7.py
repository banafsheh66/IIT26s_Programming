print("Program starting.")
Fahrenheit = float(input("Insert temperature in Fahrenheit: "))
Convert = (Fahrenheit - 32) / 1.8
Round_Convert = round(Convert, 1)
print(Fahrenheit, "°F", " is ", Round_Convert, "°C", sep="")
print("Program ending.")

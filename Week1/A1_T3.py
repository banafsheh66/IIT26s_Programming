#print(input("hi there! What is your name: "))
print("What is your name?")
name = input()
print("Hi there", name)

name=input()
print(f"Hi there {name}!")

age = input("What is your age? ")
# age = int(input("What is your age? ")) + 1
ageNext = int(age) + 1
print(f"Your age is: {age}.")
print("Your age is: " + age)
# age we is in input is string, so we can concatenate it with string
print("Your age next year will be: " + str(ageNext))


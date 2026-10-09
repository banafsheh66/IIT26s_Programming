
print("Program starting.")

Number = int(input("Insert an integer: "))
Steps = 0
print(Number)

while Number != 1:
    if Number % 2 == 0:
        Number = Number // 2 
        #floor division(7 // 2 = 3)
        #normal division(7 / 2 = 3.5)
        # modulo of 5 % 2= 1(baghimande)
    else:
        Number = Number * 3 + 1
    print(" -> ", Number, sep="", end="")
    Steps += 1
print()
print(f"Sequence had",{Steps}, "total steps.")
print()
print("Program ending.")

    
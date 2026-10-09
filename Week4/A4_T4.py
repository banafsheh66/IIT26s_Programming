
print("program starting.")

UserInput = input("Insert word (empty stops ): ")
WordCount = 0
WordCharrecters = 0

while UserInput != "":
    WordCount = WordCount + 1
    WordCharrecters = WordCharrecters + len(UserInput)
    UserInput = input("Insert word (empty stops ): ")

print("You inserted:")                 
print(f"-- {WordCount} words")
print(f"-- {WordCharrecters} characters")

print("program ending.")

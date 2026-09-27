print("Program starting.")

Word = input("Insert a closed compound word:")

Word_length = len(Word)
First_character = Word[0]
Last_character = Word[-1]
Reverse_word = Word[::-1]
Step_Size = 1

print("The word you inserted is '", Word, "' and in reverse it is '", Reverse_word, "'.", sep="", end="\n")
print("The inserted word length is ", Word_length, sep="", end="\n")
print("Last character is '", Last_character, "'", sep="", end="\n")

print("Take substring from the inserted word by inserting...")
Start_Point = int(input("1) Starting point: "))
End_Point = int(input("2) Ending point: "))
Step_Size = int(input("3) Step size: "))


print("The word '", Word, "' sliced to the defined substring is '", Word[Start_Point:End_Point:Step_Size], "'.", sep="", end="\n")
print("Program ending.")




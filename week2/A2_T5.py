print("Program starting.")

Word = input("Insert a closed compound word:")

Word_length = len(Word)
First_character = Word[0]
Reverse_word = Word[::-1]

print("The word you inserted is", Word, "and in reverse it is", Reverse_word, ".", sep=" ", end="\n")
print("The inserted word length is", Word_length, "characters long.", sep=" ", end="\n")
print("The first character is", First_character, ".", sep=" ", end="\n")

Start_Point = int(input("Enter the start index for substring: "))
End_Point = int(input("Enter the end index for substring: "))
Step_Size = int(input("Step Size is: "))

print("The word", Word, "sliced to the defined substring is", Word[Start_Point:End_Point:Step_Size], ".", sep=" ", end="\n")
print("Program ending.")

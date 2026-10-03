print("Program starting.")
print("String comparisons")
wordfirst = input("Insert first word: ")
char = input("Insert a character: ")
if char in wordfirst:
    print(f'Word "{wordfirst}" contains character "{char}"')
else:
    print(f'Word "{wordfirst}" doesn\'t have character "{char}"')
   
wordsecond = input("Insert second word: ")
if wordfirst > wordsecond:
    print(f'The second word "{wordsecond}" is before the first word "{wordfirst}" alphabetically.')
elif wordsecond > wordfirst:
    print(f'The first word "{wordfirst}" is before the second word "{wordsecond}" alphabetically.')
else:
    print(f"Both inserted words are the same alphabetically: {wordfirst}")

print("Program ending.")

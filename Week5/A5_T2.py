
def main():
    print("Program starting!")
    print()
    word = input("Insert Word: ")
    print()
    frameWord(word)

    print()
    print("Program ending.")
    return None

def frameWord(PWord):
    #print("************")
    print("*" * (len(PWord) + 4))
    print("*"+ PWord + "*")
    print("*" * (len(PWord) + 4))
    return None
main()




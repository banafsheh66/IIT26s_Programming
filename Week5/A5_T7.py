
DELIMITER = ","

def main():
    print("Program starting.")
    var = collectWords()
    analyseWords(var)
    print("Program ending.")
    return None


def collectWords():
    var = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "" or word == ".":
            break
        if var == "":
            var = word
        else:
            var += DELIMITER + word
    return var


def analyseWords(Words):
    if Words == "":
        countWords = 0
        characters = 0
        Avg = 0
    else:
        words = Words.split(DELIMITER)
        countWords = len(words)
        characters = 0

        for word in words:
            characters += len(word)

        Avg = characters / countWords

    print(f"- {countWords} Words")
    print(f"- {characters} Characters")
    print("- {:.2f} Average word length".format(Avg))
    return None


main()

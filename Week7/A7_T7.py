
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def readConfig(Filename, Rotors):
    File = open(Filename, "r")

    for Line in File:
        Line = Line.strip()
        if Line != "":
            Parts = Line.split(":")
            if Parts[0] == "Reflector":
                Reflector = Parts[1]
            else:
                Rotors.append(Parts[1])

    File.close()
    return Reflector


def rotate(Positions):
    Positions[0] += 1

    if Positions[0] == 26:
        Positions[0] = 0
        Positions[1] += 1

    if Positions[1] == 26:
        Positions[1] = 0
        Positions[2] += 1

    if Positions[2] == 26:
        Positions[2] = 0

    return None


def convertLetter(Letter, Rotors, Positions, Reflector):
    rotate(Positions)

    Number = ALPHABET.index(Letter)

    for i in range(3):
        Number = (Number + Positions[i]) % 26
        Letter = Rotors[i][Number]
        Number = (ALPHABET.index(Letter) - Positions[i]) % 26

    Letter = Reflector[Number]
    Number = ALPHABET.index(Letter)

    for i in range(2, -1, -1):
        Number = (Number + Positions[i]) % 26
        Letter = ALPHABET[Number]
        Number = (Rotors[i].index(Letter) - Positions[i]) % 26

    return ALPHABET[Number]


def main():
    Rotors = []
    Positions = [0, 0, 0]

    Filename = input("Insert config(filename): ")
    Plugs = input("Insert plugs (y/n)?: ")

    if Plugs == "n":
        print("No extra plugs inserted.")
    else:
        print("Plugboard not implemented.")

    Reflector = readConfig(Filename, Rotors)
    print("Enigma initialized.")
    print()

    Row = input("Insert row (empty stops): ")

    while Row != "":
        Positions = [0, 0, 0]
        Result = ""

        Row = Row.upper()

        for Letter in Row:
            if Letter in ALPHABET:
                NewLetter = convertLetter(
                    Letter, Rotors, Positions, Reflector
                )
                print('Character "{}" illuminated as "{}"'.format(
                    Letter, NewLetter
                ))
                Result += NewLetter
            else:
                Result += Letter

        print('Converted row - "{}".'.format(Result))
        print()

        Row = input("Insert row (empty stops): ")

    print()
    print("Enigma closing.")
    return None


main()

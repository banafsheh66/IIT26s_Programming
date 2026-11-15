
def readFile(fileName: str) -> list:
    Filehandle = open(fileName, 'r', encoding='utf-8')
    names = []

    for line in Filehandle:
        name = line.strip()

        if name != "":
            names.append(name)

    Filehandle.close()
    return names

def analyzeNames(names: list) -> dict:
    count = len(names)

    if count == 0:
     return {
        "count": 0,
        "shortest": 0,
        "longest": 0,
        "average": 0.0
    }

    lengths = []
    for name in names:
        lengths.append(len(name))
    shortest = min(lengths)
    longest = max(lengths)
    average = sum(lengths) / count
    return {
    "count": count,
    "shortest": shortest,
    "longest": longest,
    "average": average
}     

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    fileName = input("Insert filename to read: ")

    print(f'Reading names from "{fileName}".')
    names = readFile(fileName)
    print("Analysing names...")
    analysis = analyzeNames(names)
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {analysis['count']}")
    print(f"Shortest name - {analysis['shortest']} chars")
    print(f"Longest name - {analysis['longest']} chars")
    print(f"Average name - {analysis['average']:.2f} chars")
    print("Program ending.")
main()
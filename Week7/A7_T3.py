
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturnday", "Sunday")


def readFile(PFilename, PRows):
    print('Reading file "{}".'.format(PFilename))

    PRows.clear()
    file = open(PFilename, "r")

    file.readline()

    for line in file:
        line = line.strip()
        if line != "":
            PRows.append(line)

    file.close()
    return None


def analyseTimestamps(PRows, PResults):
    print("Analysing timestamps.")

    counts = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for i in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[i]):
                counts[i] += 1

    for i in range(len(WEEKDAYS)):
        PResults.append(" - {} {} stamps".format(WEEKDAYS[i], counts[i]))

    counts.clear()
    return None


def displayResults(PResults):
    print("Displaying results.")
    print("### Timestamp analysis ###")

    for result in PResults:
        print(result)

    print("### Timestamp analysis ###")
    return None


def main():
    print("Program starting.")

    Rows = []
    Results = []

    filename = input("Insert filename: ")

    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)

    Rows.clear()
    Results.clear()

    print("Program ending.")
    return None


main()


    
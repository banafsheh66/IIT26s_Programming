
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturnday", "Sunday")

DELIMITER = ";"


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0


class DAY_USAGE:
    weekday = ""
    usage = 0.0
    cost = 0.0


def readFile(PFilename, PTimestamps):
    print('Reading file "{}".'.format(PFilename))

    PTimestamps.clear()

    File = open(PFilename, "r")
    File.readline()

    for Line in File:
        Row = Line.rstrip()

        if Row != "":
            Columns = Row.split(DELIMITER)

            Timestamp = TIMESTAMP()
            Timestamp.weekday = Columns[0]
            Timestamp.hour = Columns[1]
            Timestamp.consumption = float(Columns[2])
            Timestamp.price = float(Columns[3])

            PTimestamps.append(Timestamp)
            Columns.clear()

    File.close()
    return None


def analyseTimestamps(PTimestamps, PResults):
    print("Analysing timestamps.")

    Days = []

    for Weekday in WEEKDAYS:
        Day = DAY_USAGE()
        Day.weekday = Weekday
        Day.usage = 0.0
        Day.cost = 0.0
        Days.append(Day)

    for Timestamp in PTimestamps:
        for Day in Days:
            if Timestamp.weekday == Day.weekday:
                Day.usage += Timestamp.consumption
                Day.cost += Timestamp.consumption * Timestamp.price

    for Day in Days:
        Result = " - {} usage {:.2f} kWh, cost {:.2f} €".format(
            Day.weekday, Day.usage, Day.cost
        )
        PResults.append(Result)

    Days.clear()
    return None


def displayResults(PResults):
    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for Result in PResults:
        print(Result)

    print("### Electricity consumption summary ###")
    return None


def main():
    print("Program starting.")

    Timestamps = []
    Results = []

    Filename = input("Insert filename: ")

    readFile(Filename, Timestamps)
    analyseTimestamps(Timestamps, Results)
    displayResults(Results)

    Timestamps.clear()
    Results.clear()

    print("Program ending.")
    return None


main()

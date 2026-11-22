
DELIMITER = ";"


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0


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


def displayResults(PTimestamps):
    print("Electricity usage:")

    for Timestamp in PTimestamps:
        Total = Timestamp.consumption * Timestamp.price

        print(" - {} {}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            Timestamp.weekday,
            Timestamp.hour,
            Timestamp.price,
            Timestamp.consumption,
            Total
        ))

    return None


def main():
    print("Program starting.")

    Timestamps = []

    Filename = input("Insert filename: ")

    readFile(Filename, Timestamps)
    displayResults(Timestamps)

    Timestamps.clear()

    print("Program ending.")
    return None


main()

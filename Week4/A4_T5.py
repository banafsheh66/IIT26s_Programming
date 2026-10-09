print("Program starting.")
print()

StartPoint = int(input("Insert starting point: "))
StopPoint = int(input("Insert stopping point: "))
InspectionPoint = int(input("Insert inspection point: "))
print()

if StartPoint >= StopPoint:
    print("Starting point value must be less than the stopping point value.")

elif InspectionPoint < StartPoint or InspectionPoint > StopPoint:
    print("Inspection value must be within the range of start and stop.")

else:
    print("First loop - inspection with break:")
    for i in range(StartPoint, StopPoint):
        if i == InspectionPoint:
            break
        print(i, end=" " if i + 1 != InspectionPoint else "")
    print()

    print("Second loop - inspection with continue:")
    for i in range(StartPoint, StopPoint):
        if i == InspectionPoint:
            continue
        print(i, end=" " if i != StopPoint - 1 else "")
    print()
    print()

print("Program ending.")
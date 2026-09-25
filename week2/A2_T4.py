print("Program starting.")
print("Estimate how many minutes you spent on programming...")
TaskA1_T1 = float(input("Minutes spent on Task A1_T1: "))
TaskA1_T2 = float(input("Minutes spent on Task A1_T2: "))
TaskA1_T3 = float(input("Minutes spent on Task A1_T3: "))
TaskA1_T4 = float(input("Minutes spent on Task A1_T4: "))
TasskA1_T5 = float(input("Minutes spent on Task A1_T5: "))
TaskA1_T6 = float(input("Minutes spent on Task A1_T6: "))
TaskA1_T7 = float(input("Minutes spent on Task A1_T7: "))

Sum = TaskA1_T1 + TaskA1_T2 + TaskA1_T3 + TaskA1_T4 + TasskA1_T5 + TaskA1_T6 + TaskA1_T7
Average = Sum / 7

Roun_Average = round(Average, 2)

print(f"In total you spent {Sum} minutes on programming.")
print(f"Average per task was {Roun_Average} minutes.", sep=" ", end="\n")
print(f"and same rounded to the nearest integer {round(Average)} min.")
print("Program ending.")

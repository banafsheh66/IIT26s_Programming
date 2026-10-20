print("Program starting.")

def askDimension(PPrompt: str) -> float:
    Feed = float(input(PPrompt))
    return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Width = askDimension("Insert width:")
Height = askDimension("Insert height:")
Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}²")
print("Program ending,")
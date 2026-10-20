def main():
  print("Program starting.")
  count = 0
  while True:
   showOptions()
   choice = askChoice()
   if choice == 1:
     print(f"Current count: - {count}")
   elif choice == 2:
     count += 1
     print("Count increased!")
   elif choice == 3:
       count -= 1
       print("Cleared count!")  
   elif choice == 0:
     print("Exiting program.")
     print()
     break
   else:
     print("Unknown option!")
  print("Program ending.")
  return
def showOptions():
  print("Options:")
  print("1 - Show count")
  print("2 - Increase count")
  print("3 - Reset count")
  print("0 - Exit")
  return None
def askChoice():
 Feed = input("your choice: ")
 if Feed.isnumeric():
       return int(Feed)
 else:
   return -1
  
main()
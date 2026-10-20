def main():
 print("Program starting.")

 Word = ""
 while True:

  print("Options:")
  print("1 - Insert word")
  print("2 - Show current word")
  print("3 - Show current word in reverse")
  print("0 - Exit")

  Choice = input("Your choice:")
  if Choice == "1":
   Word = input("Insert word:")
  elif Choice == "2":
   print(f'Currect word: "{Word}"')
  elif Choice == "3":
   print(f'Reversed word: "{Word[::-1]}"')
  elif Choice == "0":
   break
  else:
   print("Unknown option! try again.")
  
print("Program ending.")
main()
  

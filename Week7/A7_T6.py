
import random
random.seed(1234)

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def showMenu():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    return None


def showChoice(Name, Choice):
    print("#########################")

    if Choice == 1:
        print("{} chose rock.".format(Name))
        print(ROCK)

    elif Choice == 2:
        print("{} chose paper.".format(Name))
        print(PAPER)

    elif Choice == 3:
        print("{} chose scissors.".format(Name))
        print(SCISSORS)

    return None


def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    Name = input("Insert player name: ")

    print("Welcome {}!".format(Name))
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    print()

    Wins = 0
    Losses = 0
    Draws = 0

    Choice = -1

    while Choice != 0:
        showMenu()
        Choice = int(input("Your choice: "))

        if Choice >= 1 and Choice <= 3:
            Bot = random.randint(1, 3)

            print("Rock! Paper! Scissors! Shoot!")
            print()

            showChoice(Name, Choice)
            showChoice("RPS-3PO", Bot)

            print("#########################")
            print()

            Names = ("", "rock", "paper", "scissors")

            if Choice == Bot:
                print("Draw! Both players chose {}.".format(Names[Choice]))
                Draws += 1

            elif (Choice == 1 and Bot == 3) or \
                 (Choice == 2 and Bot == 1) or \
                 (Choice == 3 and Bot == 2):

                print("{} {} beats RPS-3PO {}.".format(
                    Name, Names[Choice], Names[Bot]))
                Wins += 1

            else:
                print("RPS-3PO {} beats {} {}.".format(
                    Names[Bot], Name, Names[Choice]))
                Losses += 1

            print()

        elif Choice != 0:
            print("Invalid choice.")
            print()

    print()
    print("Results:")
    print("{} - wins ({}), losses ({}), draws ({})".format(
        Name, Wins, Losses, Draws))

    print("RPS-3PO - wins ({}), losses ({}), draws ({})".format(
        Losses, Wins, Draws))

    print()
    print("Program ending.")
    return None


main()

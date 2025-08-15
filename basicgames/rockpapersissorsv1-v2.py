# Import Nessesities
import random

# Create List to choose from
Options = [
    "rock",
    "paper",
    "sissors",
]

# Initilize Variables
PlayerAnswer = input("Please enter Rock, Paper or sissors: ")
ComputerAnswer = random.choice(Options)
PlayerAnswer = PlayerAnswer.lower()
# Make Main Game Code
while True:
    if not PlayerAnswer.isalpha():
        print("Enter valid input for rock, paper, sissors: ")
        continue
    if PlayerAnswer not in Options:
        print("Enter valid input for rock, paper, sissors: ")
        continue
    break

# Win or Lose Mechanisim (0 = rock, 1 = paper, 2 = sissors)
if ComputerAnswer == PlayerAnswer:
    print("Its a draw")
    exit()

if ComputerAnswer == Options[0] and PlayerAnswer == Options[1]:
    print(f"I played {ComputerAnswer}, but I lost.")
    exit()

if ComputerAnswer == Options[0] and PlayerAnswer == Options[2]:
    print(f"I played {ComputerAnswer} and I win!!!")
    exit()

if ComputerAnswer == Options[1] and PlayerAnswer == Options[0]:
    print(f"I played {ComputerAnswer} and I win!!!")
    exit()

if ComputerAnswer == Options[1] and PlayerAnswer == Options[2]:
    print(f"I played {ComputerAnswer}, but I lost.")
    exit()

if ComputerAnswer == Options[2] and PlayerAnswer == Options[0]:
    print(f"I played {ComputerAnswer}, but I lost.")

if ComputerAnswer == Options[2] and PlayerAnswer == Options[1]:
    print(f"I played {ComputerAnswer} and I win!!!")
    exit()

# Import Necessities
import random

Options = ["rock", "paper", "sissors"]
PlayerScore = 0
ComputerScore = 0
rounds = input("What score do you want to play untill")
print("First to 300 wins")

# Main game loop
while PlayerScore < rounds and ComputerScore < rounds:
    # Ask player each round
    PlayerAnswer = input("Please enter Rock, Paper or sissors: ").lower()

    # Validate input
    if not PlayerAnswer.isalpha() or PlayerAnswer not in Options:
        print("Enter a valid input for rock, paper, sissors.")
        continue

    # Computer chooses
    ComputerAnswer = random.choice(Options)

    # Compare and update scores
    if ComputerAnswer == PlayerAnswer:
        print("Its a draw, no score added")
    elif (
        (ComputerAnswer == "rock" and PlayerAnswer == "paper")
        or (ComputerAnswer == "paper" and PlayerAnswer == "sissors")
        or (ComputerAnswer == "sissors" and PlayerAnswer == "rock")
    ):
        print(f"I played {ComputerAnswer}, but I lost. 50 score to you")
        PlayerScore += 50
    else:
        print(f"I played {ComputerAnswer} and I win!!! I get 50 score")
        ComputerScore += 50

    # Show current scores
    print(f"Playerscore = {PlayerScore}    Computerscore = {ComputerScore}\n")

# Announce winner
if PlayerScore > ComputerScore:
    print("You win because you have the most score")
else:
    print("I have more score and I win it all!!!")

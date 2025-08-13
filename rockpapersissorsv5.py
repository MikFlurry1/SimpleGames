# Import Necessities
import random
import os
import sys

# Variables
Options = ["rock", "paper", "sissors", "lizard"]

def startgame():
    PlayerScore = 0
    ComputerScore = 0
    while True:
        rounds_input = input("What score do you want to play until: ")
        if rounds_input.isdigit() and int(rounds_input) > 0:
            rounds = int(rounds_input)
            break
        else:
            print("Please enter a valid positive number.")
    print(f"First to {rounds} wins")

    # Main game loop
    while PlayerScore < rounds and ComputerScore < rounds:
        PlayerAnswer = input("Please enter Rock, Paper, Sissors or Lizard: ").lower()

        if not PlayerAnswer.isalpha() or PlayerAnswer not in Options:
            print("Enter a valid input for rock, paper, sissors, or lizard.")
            continue

        ComputerAnswer = random.choice(Options)

        if ComputerAnswer == PlayerAnswer:
            print("Its a draw, no score added")
        elif (
            (ComputerAnswer == "rock" and PlayerAnswer in ["paper", "lizard"]) or
            (ComputerAnswer == "paper" and PlayerAnswer in ["sissors", "lizard"]) or
            (ComputerAnswer == "sissors" and PlayerAnswer in ["rock", "lizard"]) or
            (ComputerAnswer == "lizard" and PlayerAnswer in ["rock", "paper"])
        ):
            print(f"I played {ComputerAnswer}, but I lost. 50 score to you")
            PlayerScore += 50
        else:
            print(f"I played {ComputerAnswer} and I win!!! I get 50 score")
            ComputerScore += 50

        print(f"Playerscore = {PlayerScore}    Computerscore = {ComputerScore}\n")

    if PlayerScore > ComputerScore:
        print("You win because you have the most score")
    else:
        print("I have more score and I win it all!!!")

startgame()
while True:
    doesplayerwanttoplay = input("Do you want to play again? (y or n): ").lower()
    if doesplayerwanttoplay == "y":
        print("Okay, restarting game...\n")
        startgame()
    elif doesplayerwanttoplay == "n":
        print("Okay, maybe next time!")
        break
    else:
        print("Please enter 'y' or 'n'.")
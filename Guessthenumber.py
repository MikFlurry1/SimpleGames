import random

number = random.randint(1, 100)
print("Guess the number between 1 and 100!")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congrats! You guessed it!")
        break

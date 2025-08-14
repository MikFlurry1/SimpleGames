# Import needed stuff
import random

# words for guessing
words = [
    "Lantern",
    "Breeze",
    "Quantum",
    "Velvet",
    "Glacier",
    "Mosaic",
    "Orbit",
    "Echo",
    "Nimbus",
    "Prism",
]
# randomizing
word = random.choice(words)
word = word.lower()
# guessing mechanisim
word = list(word)
print(f"The word is {str(len(word))} letters long")
usersguesses = ""
user_guess1 = input("Guess the letter 10 atempts remaining: ")
if user_guess1 in word:
    print(user_guess1 + " is in the word")
    usersguesses = user_guess1
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess2 = input("Guess the letter 9 atempts remaining: ")
if user_guess2 in word:
    print(user_guess2 + " is in the word")
    usersguesses = usersguesses + user_guess2
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess3 = input("Guess the letter 8 atempts remaining: ")
if user_guess3 in word:
    print(user_guess3 + " is in the word")
    usersguesses = usersguesses + user_guess3
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess4 = input("Guess the letter 7 atempts remaining: ")
if user_guess4 in word:
    print(user_guess4 + " is in the word")
    usersguesses = usersguesses + user_guess4
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess5 = input("Guess the letter 6 atempts remaining: ")
if user_guess5 in word:
    print(user_guess5 + " is in the word")
    usersguesses = usersguesses + user_guess5
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess6 = input("Guess the letter 5 atempts remaining: ")
if user_guess6 in word:
    print(user_guess6 + " is in the word")
    usersguesses = usersguesses + user_guess6
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess7 = input("Guess the letter 4 atempts remaining: ")
if user_guess7 in word:
    print(user_guess7 + " is in the word")
    usersguesses = usersguesses + user_guess7
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess8 = input("Guess the letter 3 atempts remaining: ")
if user_guess8 in word:
    print(user_guess8 + " is in the word")
    usersguesses = usersguesses + user_guess8
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess9 = input("Guess the letter 2 atempts remaining: ")
if user_guess9 in word:
    print(user_guess9 + " is in the word")
    usersguesses = usersguesses + user_guess9
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
user_guess10 = input("Guess the letter 1 atempts remaining: ")
if user_guess10 in word:
    print(user_guess10 + " is in the word")
    usersguesses = usersguesses + user_guess10
if sorted(set(usersguesses)) == sorted(set(word)):
    print("You guessed it")
    exit()
if sorted(set(usersguesses)) != sorted(set(word)):
    print("You lost, the word was " + "".join(word))

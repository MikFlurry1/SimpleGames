# Import needed stuff
import random

# words for guessing
with open("words.txt", "r") as file:
    text = file.read()
    words = text.split()

# randomizing
word = random.choice(words)
word = word.lower()
# guessing mechanisim
hangman = [
    """
              ___________
              | /       |
              |/        O 
              |        -|- 
              |        / \\
              |  
                """,
    """
              ___________
              | /       |
              |/        O 
              |        -|- 
              |        / 
              |  
                     """,
    """
              ___________
              | /       |
              |/        O 
              |        -|- 
              |         
              |  
                     """,
    """
              ___________
              | /       |
              |/        O 
              |         |- 
              |         
              |  
                     """,
    """
              ___________
              | /       |
              |/        O 
              |         |
              |         
              |  
                     """,
    """
              ___________
              | /       |
              |/        O 
              |          
              |        
              |  
                     """,
    """
              ___________
              | /       |
              |/         
              | YOU LOST     
              |        
              |  
                     """,
]
gussedwords = set()
attemptnumber = 0

maskedword = ""
maxattempts = 6


def stats():
    global maskedword
    maskedword = ""
    for letter in word:
        if letter in gussedwords:
            maskedword += letter
        else:
            maskedword += "_"


def display():
    print(f"Word:{maskedword}")
    print(f"You have {str(maxattempts - attemptnumber)} attempts remaining")
    print(hangman[attemptnumber])


print(f"The word is {str(len(word))} letters long")
while attemptnumber < maxattempts and maskedword != word:
    stats()
    display()
    nextguess = input("Please guess a letter: ")
    if not nextguess.isalpha() or len(nextguess) != 1:
        print("Please enter a single letter, not a number or symbol.")
        continue
    if nextguess in gussedwords:
        print(f"You already guessed '{nextguess}'. Try a different letter.")
        continue
    gussedwords.add(nextguess)
    attemptnumber += 1
    stats()
if maskedword == word:
    print("Congrats you guessed the word")
else:
    print(hangman[6])
    print(f"The word was {word}, sorry")

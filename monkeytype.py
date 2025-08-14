import time
import difflib
import random

sentences = [
    "the quick brown fox jumps over the lazy dog",
    "A bird in the hand is worth two in the bush.",
    "Just staying one day ahead of yesterday.",
    "More haste, less speed.",
]
start_input = input("Do you want to start y/n: ").lower()
if start_input == "y":
    max_time = 10
    sentence = random.choice(sentences)
    lenofsentence = len(sentence)
    print(f"You have {max_time} seconds to type : {sentence}.")
    start_time = time.time()
    typed = input("Type this sentence: ").lower()
    end_time = time.time()
    time_taken = end_time - start_time
    accuracy = difflib.SequenceMatcher(None, sentence, typed).ratio() * 100
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    timeinminutes = time_taken / 60
    print(f"WPM : {(lenofsentence/5) / timeinminutes}")
    if accuracy == 100 and time_taken <= max_time:
        print("YOU DID IT PERFECTLY!")
    elif time_taken > max_time:
        print("Took a WHILE")
    else:
        print("Try to be more accurate next time!")
elif start_input == "n" :
    print("maybe next time")
    

import time
import random
from difflib import SequenceMatcher
sentences = [
    "the quick brown fox jumps over the lazy dog",
    "A bird in the hand is worth two in the bush",
    "Just staying one day ahead of yesterday",
    "More haste, less speed",
]
start_input = input("Do you want to start y/n: ").lower()

if start_input == "y":
    max_time = 10
    sentence = random.choice(sentences)
    lenofsentence = len(sentence)
    print(f"You have to type: {sentence}")

    start_time = time.time()
    typed = input("Type this sentence: ")
    end_time = time.time()
    matcher = SequenceMatcher(None, sentence, typed)   
    similarity_ratio = matcher.ratio() 
    time_taken = end_time - start_time
    accuracy = similarity_ratio * 100
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    time_in_minutes = time_taken / 60
    wpm = (lenofsentence / 5) / time_in_minutes
    print(f"WPM: {wpm:.2f}")
    if accuracy == 100 and time_taken <= max_time:
        print("YOU DID IT PERFECTLY!")
    elif time_taken > max_time:
        print("Took a WHILE")
    else:
        print("Try to be more accurate next time")

    

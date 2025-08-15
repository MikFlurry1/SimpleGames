import random

words1 = input("Enter first word: ")
words2 = input("Enter second word: ")

list1 = list(words1)
list2 = list(words2)

max_attempts = 999999999999999999999999
attempts = 0

while attempts < max_attempts:
    attempts += 1
    random.shuffle(list1)
    if "".join(list1) == words2:
        print("Anagram detected")
        break
else:
    print("Not an anagram")

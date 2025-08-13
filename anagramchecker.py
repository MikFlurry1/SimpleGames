words = input("enter first word : ")
words2 = input("enter second word : ")
wordsalpha = sorted(words)
words2alpha = sorted(words2)
if wordsalpha == words2alpha:
    print("anagram detected")
if wordsalpha != words2alpha:
    print("no anagram detected")

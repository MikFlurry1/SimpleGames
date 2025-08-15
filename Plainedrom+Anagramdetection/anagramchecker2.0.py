words1 = input("Enter first word: ")
words2 = input("Enter second word: ")


def charectercounter(input):
    counter = {}
    for i in input:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
    return counter


count_word1 = charectercounter(input=words1)
count_word2 = charectercounter(input=words2)

if count_word1 == count_word2:
    print("anagram found")
else:
    print("not an anagram")

# list1 = list(words1.replace(" ", "").lower())
# list2 = list(words2.replace(" ", "").lower())
# print("word:")
# for i in list1:
#     print(i)
# print("word2:")
# for i in list2:
#     print(i)

# # Check if sorted lists are equal (anagram test)
# if sorted(list1) == sorted(list2):
#     print("Anagram detected!")
# else:
#     print("Not an anagram.")

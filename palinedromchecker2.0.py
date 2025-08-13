text = input("Write text here, and we will tell you if it is a palindrome or not: ")
# so if there is a different in upper and lower case so it will be correct
text_lower = text.lower()
length = len(text_lower)

is_palindrome = True
for i in range(length // 2):
    if text_lower[i] != text_lower[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

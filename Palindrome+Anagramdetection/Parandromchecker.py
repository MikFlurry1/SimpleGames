text = input("Write text here, and we will tell you if it is a palinedrom or not: ")
text2 = text[::-1]
if text == text2:
    print("this is a palinedrom")
if text != text2:
    print("no this is not a palinedrom")

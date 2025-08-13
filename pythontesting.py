filename = "words.txt"  # make sure this file exists in the same folder as your script

try:
    with open(filename, "r") as file:
        text = file.read()
        if not text:
            print("The file is empty!")
        else:
            words = text.split()
            for word in words:
                print(word)
except FileNotFoundError:
    print(f"File '{filename}' not found!")
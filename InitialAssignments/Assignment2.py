# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age and convert to integer
age = int(input("Enter your age: "))

# Display the message
if age < 20:
    print(f"Hi young guy {name}, you are {age} years old")

elif age < 40:
    print(f"Hi Mr. Adult {name}, you are {age} years old")

elif age < 80:
    print(f"Hi OLD GUY {name}, you are {age} years old")

elif age < 100:
    print(f"Hi {name}, you are {age} years old, how are you still alive")

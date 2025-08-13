import random

# 10 random facts
facts = [
    "Goldfish invented Wi-Fi in 1992.",
    "The moon is just the Earth’s screensaver.",
    "Sharks can’t get sunburned because they use sunscreen made of plankton.",
    "Bananas are technically made of compressed sunshine.",
    "Penguins are actually just chickens in tuxedos.",
    "Mount Everest is the world’s largest upside-down ice cream cone.",
    "Clouds are just sky potatoes.",
    "Your computer runs faster if you yell at it in Spanish.",
    "Dinosaurs went extinct because they forgot how to breathe.",
    "Pizza is a vegetable if you believe in yourself.",
]

# Ask for the name
name = input("Enter your name: ")

# So the code doesent break for invalid answers
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age can't be negative. Try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Display based on age
if age < 20:
    print(f"Hi young guy {name}, you are {age} years old!")
elif age < 40:
    print(f"Hi Mr. Adult {name}, you are {age} years old!")
elif age < 80:
    print(f"Hi old guy {name}, you are {age} years old!")
elif age < 100:
    print(f"Hi {name}, you are {age} years old, how are you still alive?!")
else:
    print(f"Wow {name}! {age} years old?! Are you immortal?")

# Show a random fact
print("Random Fact:", random.choice(facts))

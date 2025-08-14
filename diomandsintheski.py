height = int(input("Enter the height of the diamond (half of it): "))

lines = []

# Top half
for i in range(1, height + 1):
    line = " " * (height - i) + "*" * (2 * i - 1)
    lines.append(line)

# Bottom half
for i in range(height - 1, 0, -1):
    line = " " * (height - i) + "*" * (2 * i - 1)
    lines.append(line)

# Print the diamond
for line in lines:
    print(line)
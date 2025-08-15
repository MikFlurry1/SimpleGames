height = int(input("Enter the height of the pyramid: "))
pyramid = []
for i in range(height):
    line = " " * (height - i - 1) + "*" * (2 * i + 1)
    pyramid.append(line)
for row in pyramid:
    print(row)
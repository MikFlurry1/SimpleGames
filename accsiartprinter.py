height = int(input("Enter the height of the pyramid: "))
for i in range(1, height * 2, 2):
    line = ""
    for _ in range(i) :
        line += "*"
    print((line).center(height * 2 - 1))
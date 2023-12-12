from cs50 import get_int

while True:
    input = get_int("Height: ")
    if input > 0 and input < 9:
        break

spaces = input - 1
row = 1
for i in range(input):
    for j in range(input):
        if spaces > j:
            print(" ", end="")
        else:
            print("#", end="")
    print("  ", end="")
    for j in range(row):
        print("#", end="")
    print()
    row += 1
    spaces -= 1

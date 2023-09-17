# ask user for size of the triangle and print a right angle triangle

size = int(input("kitna bara triangle?"))
for row in range(1,size+1):
    for column in range(row):
        print("#", end="")
    print()
#convert the pyramid code to only use while loop

size = int(input("kitna bara pyramid?"))
row = 1
space = size - 1
while row <= size:
    print(" "*space, end="")
    print("#"*(2*row-1))
    space = space - 1
    row += 1
# 04. ask user for the size of the pyramid and output a pyramid of that height

size = int(input("kitna bara pyramid?"))
for row in range(1,size+1):
    for space in reversed(range(row, size)):
        print(" ", end="")
    for column in range(2*row-1):
       print("#", end="")
    print()
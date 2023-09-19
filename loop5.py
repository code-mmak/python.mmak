# Q5 ask user for no. of fish and sizes of fish and print that many fish


size = int(input("kitni bara fish?"))
for row in range(1,size+1):
    for space in reversed(range(row, size)):
        print(" ", end="")
    for column in range(2*row-1):
       print("#", end="")
    print()
for revrow in reversed(range(1,size)):
    for space in reversed(range(revrow, size)):
        print(" ", end="")
    for column in range(2*revrow-1):
       print("#", end="")
    print()
for row in range(2,size+1):
    for space in reversed(range(row, size)):
        print(" ", end="")
    for column in range(2*row-1):
       print("#", end="")
    print()

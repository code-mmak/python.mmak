# Make a recursive function that counts down from the parameter given till 1

def recursiveFunction(num):
    print(num)
    if num >= 2:
        recursiveFunction(num-1)

recursiveFunction(6)
# Make a recursive function that returns the sum of all values from 1 to parameter number

def sumAll(num):
    if num > 1:
        return num + sumAll(num-1)
    else:
        return 1

print(sumAll(5))
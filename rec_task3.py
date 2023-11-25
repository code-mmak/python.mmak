# make a recursive function that takes a position number value as input and outputs fibonacci sequence
# till that position

def fib(num):
    if num <= 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(7))
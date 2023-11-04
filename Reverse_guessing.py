# create a reverse number guessing game, use random to create secret number
# output how many tries does it take

from random import randint

secNum = int(input("input the secret number"))
guessNum = -1
count = 0

while guessNum != secNum:
    guessNum = randint(1,100)
    count += 1
print(f"it took me {count} tries to guess your number")

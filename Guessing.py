#create a number guessing game, use random to create secret number
#output how many tries does it take

from random import randint

secNum = randint(0,100)
guessNum = -1
count = 0

while guessNum != secNum:
    guessNum = int(input("What's your guess?"))
    count += 1
print(f"it took you {count} tries to guess the number")
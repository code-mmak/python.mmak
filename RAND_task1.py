#Task1: Convert the rock, paper, scissor game to be only be one player.
#use random for computer input
import random
n = int(input("how many rounds?"))
for i in range(n):
    plyr_1 = input("rock paper scissor shoot(player1):")
    plyr_2 = random.randint(1,3)
    if plyr_1 == plyr_2:
        print("it's a draw")
    elif plyr_1 == "paper":
        if plyr_2 == 1:
            print("player 1 won")
        elif plyr_2 == 2:
            print("player 2 won")
    elif plyr_1 == "rock":
        if plyr_2 == 3:
            print("player 2 won")
        elif plyr_2 == 2:
            print("player 1 won")
    elif plyr_1 == "scissor":
        if plyr_2 == 1:
            print("player 2 won")
        elif plyr_2 == 3:
            print("player 1 won")

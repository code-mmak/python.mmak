#make a 2 player rock paper scissor game that runs for n rounds.
#ask user for n value, add winner for each round

n = int(input("how many rounds?"))
for i in range(n):
    plyr_1 = input("rock paper scissor shoot(player1):")
    plyr_2 = input("rock paper scissor shoot(player2):")
    if plyr_1 == plyr_2:
        print("it's a draw")
    elif plyr_1 == "paper":
        if plyr_2 == "rock":
            print("player 1 won")
        elif plyr_2 == "scissor":
            print("player 2 won")
    elif plyr_1 == "rock":
        if plyr_2 == "paper":
            print("player 2 won")
        elif plyr_2 == "scissor":
            print("player 1 won")
    elif plyr_1 == "scissor":
        if plyr_2 == "rock":
            print("player 2 won")
        elif plyr_2 == "paper":
            print("player 1 won")


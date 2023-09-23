# convert rock paper scissor game to only use while loop

n = int(input("how many rounds?"))
plyr_1score=0
plyr_2score=0
round =  1
while round <= n :
    plyr_1 = input("rock paper scissor shoot(player1):")
    plyr_2 = input("rock paper scissor shoot(player2):")
    if plyr_1 == plyr_2:
        print("it's a draw")
    elif plyr_1 == "paper":
        if plyr_2 == "rock":
            print("player 1 won")
            plyr_1score += 1
        elif plyr_2 == "scissor":
            print("player 2 won")
            plyr_2score += 1
    elif plyr_1 == "rock":
        if plyr_2 == "paper":
            print("player 2 won")
            plyr_2score += 1
        elif plyr_2 == "scissor":
            print("player 1 won")
            plyr_1score += 1
    elif plyr_1 == "scissor":
        if plyr_2 == "rock":
            print("player 2 won")
            plyr_2score +=1
        elif plyr_2 == "paper":
            print("player 1 won")
            plyr_1score += 1
    round +=1
print(f"player 1 score is: {plyr_1score}")
print(f"player 2 score is: {plyr_2score}")
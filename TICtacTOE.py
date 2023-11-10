Game = [["_" for col in range(3)]for row in range(3)]
print("x for player 1 and o for player 2")
tries = 0
end = False

while end == False and tries < 9:
    row = int(input("enter row for player 1: "))
    col = int(input("enter column for player 1: "))
    Game[row][col] = "x"
    for row in range(3):
        print(Game[row][0], Game[row][1], Game[row][2])

    for row in range(3):

        o_count = 0
        x_count = 0
        for col in range(3):
            if Game[row][col] == "o":
                o_count +=1
            elif Game[row][col] == "x":
                x_count +=1
        if o_count == 3:
            print("player 2 won")
            end = True
        elif x_count == 3:
            print("player 1 won")
            end = True
    for col in range(3):
        o_count = 0
        x_count = 0
        for row in range(3):
            if Game[row][col] == "o":
                o_count +=1
            elif Game[row][col] == "x":
                x_count +=1
        if o_count == 3:
            print("player 2 won")
            end = True
        elif x_count == 3:
            print("player 1 won")
            end = True


    if end:
        break
    elif (Game[0][0] and Game[1][1] and Game[2][2] == "x") or (Game[0][2] and Game[1][1] and Game[2][0] == "x"):
        print("player 1 won")
        break
    elif (Game[0][0] and Game[1][1] and Game[2][2] == "o") or (Game[0][2] and Game[1][1] and Game[2][0] == "o"):
        print("player 2 won")
        break
    row = int(input("enter row for player 2: "))
    col = int(input("enter column for player 2: "))
    Game[row][col] = "o"
    for row in range(3):
        print(Game[row][0], Game[row][1], Game[row][2])
    for row in range(3):

        o_count = 0
        x_count = 0
        for col in range(3):
            if Game[row][col] == "o":
                o_count +=1
            elif Game[row][col] == "x":
                x_count +=1
        if o_count == 3:
            print("player 2 won")
            end = True
        elif x_count == 3:
            print("player 1 won")
            end = True
    for col in range(3):
        o_count = 0
        x_count = 0
        for row in range(3):
            if Game[row][col] == "o":
                o_count +=1
            elif Game[row][col] == "x":
                x_count +=1
        if o_count == 3:
            print("player 2 won")
            end = True
        elif x_count == 3:
            print("player 1 won")
            end = True


    if end:
        break
    elif (Game[0][0] and Game[1][1] and Game[2][2] == "x") :
        print("player 1 won")
        break
    elif (Game[0][2] and Game[1][1] and Game[2][0] == "x"):
        print("player 1 won")
        break
    elif (Game[0][0] and Game[1][1] and Game[2][2] == "o"):
        print("player 2 won")
        break
    elif (Game[0][2] and Game[1][1] and Game[2][0] == "o"):
        print("player 2 won")
        break
    tries +=1

if not end:
    print("it's a tie")
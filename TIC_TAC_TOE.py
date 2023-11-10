#TASK6: make a 2 player tic tac toe

Game = [["" for col in range(3)]for row in range(3)]
print("x for player 1 and o for player 2")
tries = 0
end = False
while end == False and tries < 9:
    row = int(input("enter row for player 1: "))
    col = int(input("enter column for player 1: "))
    Game[row][col] = "x"
    for row in range(3):
        print(Game[row][0], Game[row][1], Game[row][2])
    if Game[0][0] and Game[0][1] and Game[0][2] == "x" or Game[1][0] and Game[1][1] and Game[1][2] == "x" or Game[2][0] and Game[2][1] and Game[2][2] == "x" or Game[0][0] and Game[1][1] and Game[2][2] == "x" or Game[0][2] and Game[1][1] and Game[2][0] == "x" or Game[0][0] and Game[1][0] and Game[2][0] == "x" or Game[0][1] and Game[1][1] and Game[2][1] == "x" or Game[0][2] and Game[1][2] and Game[2][2] == "x":
        print("player 1 won")
        end = True
        break

    row = int(input("enter row for player 2: "))
    col = int(input("enter column for player 2: "))
    Game[row][col] = "o"
    if (Game[0][0] and Game[0][1] and Game[0][2] == "o") or (Game[1][0] and Game[1][1] and Game[1][2] == "o") or (Game[2][0] and Game[2][1] and Game[2][2] == "o") or (Game[0][0] and Game[1][1] and Game[2][2] == "o") or (Game[0][2] and Game[1][1] and Game[2][0] == "o") or (Game[0][0] and Game[1][0] and Game[2][0] == "o") or (Game[0][1] and Game[1][1] and Game[2][1] == "o") or (Game[0][2] and Game[1][2] and Game[2][2] == "o"):
        print("player 2 won")
        end = True
    for row in range(3):
        print(Game[row][0], Game[row][1], Game[row][2])

    tries += 1




total = 0
userInput = int(input("enter a number:"))
while userInput!=0:
    if userInput % 2==0:
        total = total + userInput
    else:
        total = total + userInput
    prime = True 
    for i in range(2, userInput):
        if userInput % i == 0:
            prime = False
    if prime:
        total = total * userInput
    userInput = int(input("enter a number:"))

print("the total is", total)

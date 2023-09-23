#ask user to think of a number between 1-100
#your program can ask yes or no questions (max 10)
#your program should tell the correct guess everytime

# no of digits
# even or odd

if input("is it a 1 digit no?") == "yes":

        if input("is it even?") == "yes":
            less_than5 = input("is it less than 5?")
            if less_than5  == "yes":
                if input("is it divisible by 4?") == "yes":
                    print("your number is 4")
                else:
                    print("your number is 2")
            elif less_than5 == "no":
                if input("is it divisible by 8") == "yes":
                    print("your number is 8")
                elif input("is it divisible by 6")=="yes":
                    print("your number is 6")
                else:
                    print("your number is 5")
        else:
            less_than5 = input("is it less than 5?")
            if less_than5 == "yes":
                if input("is it divisible by 3?") == "yes":
                    print("your number is 3")
                else:
                    print("your number is 1")
            elif less_than5 == "no":
                if input("is it divisble by 9") == "yes":
                    print("your number is 9")
                elif input("is it divisble by 7?") == "yes":
                    print("your number is 7")
                else:
                    print("your number is 5")

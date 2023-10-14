#TASK 1: Ask user for a string and output if the string is palindrome
str = input("enter a palindrome: ").lower()
is_palindrome = False
for i in range(len(str)):
    if str[:i] == str[-i:]:
        is_palindrome = True
if is_palindrome:
    print("it is a palindrome")
else:
    print("not a palindrome")
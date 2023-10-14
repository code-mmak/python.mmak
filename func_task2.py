#Task2: Ask user for a string, convert and store it in reverse
inString = input("enter a prompt:")
newString = ""

for i in range(len(inString)-1, -1, -1):
    newString = newString + inString[i]
print(newString)

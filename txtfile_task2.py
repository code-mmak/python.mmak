FileHandle = open("names.txt", "r")
NewFile = open("favnames.txt", "w")
for i in range(10):
    name = FileHandle.readline().strip()
    if len(name) < 5:
        NewFile.write(name + "\n")
FileHandle.close()
NewFile.close()
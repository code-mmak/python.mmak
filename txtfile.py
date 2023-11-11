#open(fileName, mode)
# w = write (create files/re-creates file, store data)
# r = read (req: file should already exist, fetches data)
# a = append (req: file should already exist, adds data at the end of file)

FileHandle = open("SampleFile.TXT", "w")
FileHandle.write("Line of text \n")
FileHandle.close()

#Task: Creat a file called "names.txt", ask user to store 10 names in the file

FileHandle = open("names.txt", "w")
for i in range(11):
    name = input("enter name: ")
    FileHandle.write(name + "\n")

FileHandle.close()



FileHandle = open("SampleFile.TXT", "r")
LineOfText = FileHandle.readline()
print(LineOfText)
FileHandle.close()

#Task: read file "names.txt" and copy all names with less than 5 characters in a new file
# "favnames.txt"


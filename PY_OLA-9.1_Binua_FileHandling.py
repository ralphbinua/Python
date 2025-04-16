print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

def appendFile():
    appendFile = open("file.txt", "a") # write in the end of the file

    name = input("Enter a Name: ")
    email = input("Enter Email Address: ")
    address = input("Enter Home Address: ")
    appendFile.write("\n" + name + ", " + email + ", " + address)

def openFile():
    openFile = open("file.txt", "r") # read the txt file
    print( "\n"+ openFile.read())

def writeFile():
    writeFile = open("file.txt", "w") # clear the record
    writeFile.write("No records found!")

print("RECORD KEEPING APP")

while True:
    print("A. Add a record")
    print("B. View all record")
    print("C. Clear all records")
    print("D. Exit")

    userInput = input("\nEnter a choice: ")

    if userInput.upper() == 'A': appendFile()
    elif userInput.upper() == 'B': openFile()
    elif userInput.upper() == 'C': writeFile()
    elif userInput.upper() == 'D':
        print("Thank you!")
        break
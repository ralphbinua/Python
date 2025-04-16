print("Ralph Gabriel B. Binua")
print("2BSIT-3\n")

dictionary = {}

print("Dictionary")

def addData():
        keyValue = input("Enter Key Value: ")
        value = input("Enter value: ")
        dictionary[keyValue] = value
        print(dictionary, '\n')

def deleteData():
        deleteKeyValue = input("Enter Delete Key Value: ")
        deleteValue = input("Enter Delete value: ")
        dictionary.pop(deleteKeyValue, deleteValue)
        print(dictionary, '\n')
      
while True:
    print("A. Add Data")
    print("B. Delete Data")
    print("C. End")
    
    userInput = input("\nEnter a choice: ")

    if userInput.upper() == 'A': addData()
    elif userInput.upper() == 'B': deleteData()
    elif userInput.upper() == 'C': break
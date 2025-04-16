print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

listWord = []
listCount = 0

while True:
    word = input("Enter a word: ")
    print("You entered the word", word)
    listWord.append(word)
    listCount += 1

    choices = input("Do you want to try again? [Y/N]: ")

    if choices.upper() == 'N':
        break

print("You entered", listCount, "words:")

for list in listWord:
    print(list)
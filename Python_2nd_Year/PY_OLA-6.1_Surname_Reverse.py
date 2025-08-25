print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

word = input("Enter a word / words: ")

def reverseString(inputWord):
    return inputWord[::-1]

reversedWord = reverseString(word)
characterCount = len(word)

print("STRING: " + word)
print("REVERSED: " + reversedWord + " "+str(characterCount) + " CHARACTERS")
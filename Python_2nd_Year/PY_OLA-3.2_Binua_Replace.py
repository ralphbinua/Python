print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

print("Nouns")
firstNoun = input("Enter the first noun: ").upper()
secondNoun = input("Enter the second noun: ").upper()
thirdNoun = input("Enter the third noun: ").upper()

print("------------------\n")

print("Adjectives")
firstAdjective = input("Enter the first Adjective: ").upper()
secondAdjective = input("Enter the second Adjective: ").upper()
thirdAdjective = input("Enter the third Adjective: ").upper()

print("------------------\n")

print("Original Song")
originalSong = "Twinkle twinkle little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky"
print(originalSong)
print("------------------\n")

print("Edited Song")
originalSong = "Twinkle twinkle {} {}\nHow I wonder what you are\nUp above the {} so {}\nLike a {} in the {}"
newOriginalSong = originalSong.format(firstAdjective, firstNoun, secondNoun, secondAdjective, thirdAdjective, thirdNoun)
print(newOriginalSong)
print("------------------\n")
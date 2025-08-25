print("Binua, Ralph Gabriel B.")
print("2BSIT-3")

studentName = input("LN, FN MI: ")
print("Enter student's grade in")
mathGrade = float(input("Math: "))
scienceGrade = float(input("Science: "))
englishGrade = float(input("English: "))

averageGrade = (mathGrade + scienceGrade + englishGrade) / 3
print("Average grade of " + studentName + " is " + str(averageGrade))
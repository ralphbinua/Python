print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

while True:
    name = input("Enter Name of student (or type exit): ")
    if name.lower() == 'exit':
        break

    print("Enter Grades")
    math_grade = float(input(f"\tMath: "))
    english_grade = float(input(f"\tEnglish: "))
    science_grade = float(input(f"\tScience: "))

    average = (math_grade + english_grade + science_grade) / 3

    print(f"\n{name}'s grades\n\tMath = {math_grade}, English = {english_grade}, Science = {science_grade}")
    print(f"\tAverage = {average:.2f}\n")
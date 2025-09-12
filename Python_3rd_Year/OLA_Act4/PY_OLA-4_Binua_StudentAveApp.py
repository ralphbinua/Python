print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

class Student:
    def __init__(self, name, mathGrade, ScienceGrade, EnglishGrade):
        self.name = name
        self.mathGrade = mathGrade
        self.ScienceGrade = ScienceGrade
        self.EnglishGrade = EnglishGrade

    def average(self):
        return (self.mathGrade + self.ScienceGrade + self.EnglishGrade) / 3

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Math Grade: {self.mathGrade}")
        print(f"Science Grade: {self.ScienceGrade}")
        print(f"English Grade: {self.EnglishGrade}")
        print(f"Average Grade: {self.average()}")

name = input("Enter Student Name: ")
mathGrade = float(input("Enter Math Grade: "))
ScienceGrade = float(input("Enter Science Grade: "))
EnglishGrade = float(input("Enter English Grade: "))
student = Student(name, mathGrade, ScienceGrade, EnglishGrade)
student.display()
import PY_OLA_1B_Surname_Deductions as deductions

print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

rate_perhour = 500

name = input("Name: ")
hour = float(input("Hours worked: "))

#gross salary
gross_salary = rate_perhour * hour
print("Gross Salary: Php " + str(gross_salary))
deductions.deduction_salary(gross_salary)
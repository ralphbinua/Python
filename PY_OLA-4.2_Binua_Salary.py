print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

empName = input("Enter Name: ")
hours = int(input("Enter number of hours: "))
sssContri = int(input("SSS contribution: "))
philHealth = int(input("Phil health: "))
housingLoan = int(input("Housing loan: "))
rateHour = 500
tax = 500

totalEarnings = hours * rateHour
totalDeductions = sssContri + philHealth + housingLoan + tax
netPay = totalEarnings - totalDeductions

print("\n=====PAYSLIP=====")
print("=====EMPLOYEE INFORMATION=====")
print("Employee Name: " + empName)
print("Rendered Hours: " + str(hours))
print("Rate per hour: " + str(rateHour))
print("Gross Salary: " + str(totalEarnings))

print("\n=====DEDUCTIONS=====")
print("SSS: " + str(sssContri))
print("Phil health: " + str(philHealth))
print("Other Loan: " + str(housingLoan))
print("Total Deductions: " + str(totalDeductions))
print("Net Salary: " + str(netPay))
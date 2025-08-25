#   Binua, Ralph Gabriel B.
#   3BSIT-5

import PY_OLA_1C_Binua_NetSalary as netsalary

tax_deduction = 0.12

def deduction_salary(salary):
    salary = float(salary)
    tax = salary * tax_deduction
    print("Tax: Php " + str(tax))
    loan = float(input("Loan: Php "))
    insurance = float(input("Insurance: Php "))
    total_deduction = tax + loan + insurance
    print("Total Deductions: Php " + str(total_deduction))
    netsalary.net_salary(salary, total_deduction)
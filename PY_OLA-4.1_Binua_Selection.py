print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

empName = input("Enter employee name: ")
yrService = int(input("Enter years-in-service: "))
office = input("Enter office (IT, ACCT, HR): ").upper()

if office == 'IT':
    if yrService >= 10:
        print("Hi, " + empName + ", your bonus is 10000")
    else:
        print("Hi, " + empName + ", your bonus is 5000")

elif office == 'ACCT':
    if yrService >= 10:
        print("Hi, " + empName + ", your bonus is 12000")
    else:
        print("Hi, " + empName + ", your bonus is 6000")

elif office == 'HR':
    if yrService >= 10:
        print("Hi, " + empName + ", your bonus is 15000")
    else:
        print("Hi, " + empName + ", your bonus is 7500")
else:
    print("Invalid office entered.")
print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")


import PY_OLA_9_Binua_Power as power
import PY_OLA_9_Binua_Remainder as remainder
import PY_OLA_9_Binua_Quotient as quotient
import PY_OLA_9_Binua_Absolute as absolute


while True:
    try:
        print("Simple Arithmetic Operations")
        print("1. Power")
        print("2. Remainder")
        print("3. Quotient")
        print("4. Absolute")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            power.power()
        elif choice == '2':
            remainder.remainder()
        elif choice == '3':
            quotient.quotient()
        elif choice == '4':
            absolute.absolute()
        elif choice == '5':
            print("Thank You")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
            continue
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank You")
            break
    except Exception as e:
        print("An error occurred:", e)
        continue
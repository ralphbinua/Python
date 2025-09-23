print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

import PY_OLA_10_Binua_CummulativeSummation as cummulative_summation
import PY_OLA_10_Binua_Ceiling as ceiling
import PY_OLA_10_Binua_Floor as floor
import PY_OLA_10_Binua_Rounding as  rounding
import PY_OLA_10_Binua_Summation as summation
import PY_OLA_10_Binua_Truncation as truncation

while True:
    try:
        print("Rounding Decimal")
        print("1. Truncation")
        print("2. Rounding")
        print("3. Floor")
        print("4. Ceiling")
        print("5. Summation")
        print("6. Cumulative Summation")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        if choice == '1':
            truncation.truncation()
        elif choice == '2':
            rounding.rounding()
        elif choice == '3':
            floor.floor()
        elif choice == '4':
            ceiling.ceiling()
        elif choice == '5':
            summation.summation()
        elif choice == '6':
            cummulative_summation.cummulative_summation()
        elif choice == '7':
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
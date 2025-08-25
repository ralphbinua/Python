print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

def divide(numOne, numTwo):
    return numOne / numTwo

def addition(numOne, numTwo):
    return numOne + numTwo

def subtraction(numOne, numTwo):
    return numOne - numTwo

def multiplication(numOne, numTwo):
    return numOne * numTwo

while True:
    try:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            numOne = float(input("Enter the first number: "))
            numTwo = float(input("Enter the second number: "))
            result = addition(numOne, numTwo)
            print(f"The result of addition is: {result}")

        elif choice == '2':
            numOne = float(input("Enter the first number: "))
            numTwo = float(input("Enter the second number: "))
            result = subtraction(numOne, numTwo)
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            numOne = float(input("Enter the first number: "))
            numTwo = float(input("Enter the second number: "))
            result = multiplication(numOne, numTwo)
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            numOne = float(input("Enter the first number: "))
            numTwo = float(input("Enter the second number: "))

            if numTwo == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            else:
                result = divide(numOne, numTwo)
                print(f"The result of division is: {result}")
        elif choice == '5':
            print("Thank You")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
            continue

        # Ask if the user wants to continue
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank You")
            break

    except ZeroDivisionError as e:
        print(e)
        continue

    except Exception:
        print("Invalid input. Please select a valid operation.")
        continue
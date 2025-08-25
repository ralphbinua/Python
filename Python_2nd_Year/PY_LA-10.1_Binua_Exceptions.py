print("Binua, Ralph Gabriel B.")
print("2BSIT-3\n")

def calculator():
    while True:
        try:
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = input("Enter your choice (1/2/3/4): ")
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = num1 / num2
                print(f"The result of division is: {result}")

            while True:
                try_again = input("Do you want to try again? (y/n): ").strip().lower()
                if try_again == 'y':
                    break
                elif try_again == 'n':
                    print("Thank You")
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

calculator()
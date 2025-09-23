def array():
    try:
        arraySize = int(input("Enter the size of the arrays: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    arr1 = []
    arr2 = []

    for i in range(arraySize):
        while True:
            try:
                num1 = int(input(f"Enter element {i+1} of the first array: "))
                arr1.append(num1)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                num2 = int(input(f"Enter element {i+1} of the second array: "))
                arr2.append(num2)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    print("\nArray 1:", arr1)
    print("Array 2:", arr2)
    return arr1, arr2
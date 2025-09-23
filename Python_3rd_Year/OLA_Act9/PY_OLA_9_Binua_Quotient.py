import PY_OLA_9_Binua_Array as array
import numpy as np

def quotient():
    arr1, arr2 = array.array()
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    quotient, remainder = np.divmod(arr1, arr2)
    print("\nQuotient of elements in Array 1 divided by corresponding elements in Array 2:")
    print(quotient)
    print("Remainder of elements in Array 1 divided by corresponding elements in Array 2:")
    print(remainder)
    return
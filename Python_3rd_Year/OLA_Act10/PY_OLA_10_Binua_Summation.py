import PY_OLA_10_Binua_Array as array
import numpy as np

def summation():
    arr1, arr2 = array.array2()
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    newarr = np.add(arr1, arr2)
    print("\nSummation of elements in Array 1 and Array 2:")
    print("Array 1:", newarr)
    return
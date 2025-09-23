import PY_OLA_9_Binua_Array as array
import numpy as np

def power():
    arr1, arr2 = array.array()
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    newarr = np.power(arr1, arr2)
    print("\nPower Value is:", newarr)
    return
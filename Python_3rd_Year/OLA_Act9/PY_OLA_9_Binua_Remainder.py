import PY_OLA_9_Binua_Array as array
import numpy as np

def remainder():
    arr1, arr2 = array.array()
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    print("\nRemainder of elements in Array 1 divided by corresponding elements in Array 2:")
    print(np.remainder(arr1, arr2))
    return
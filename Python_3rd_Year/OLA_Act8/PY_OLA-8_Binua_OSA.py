print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# Other Simple Arithmetic

import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([1, 2, 2, 3, 1, 2])
newarr = np.power(arr1, arr2)
print("np.power", newarr)

a = np.array([10, -20, 30, -40, 50, -60])
b = np.array([3, 5, 10, 8, 2, 33])

print("np.mod:", np.mod(a, b))
print("np.remainder:", np.remainder(a, b))

quotient, remainder = np.divmod(a, b)
print("np.divmod quotient:", quotient)
print("np.divmod remainder:", remainder)

print("np.absolute:", np.absolute(a))
print("np.abs:", np.abs(a))
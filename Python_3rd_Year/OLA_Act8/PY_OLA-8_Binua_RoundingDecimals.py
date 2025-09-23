print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# Rounding Decimals

import numpy as np

arr = np.array([3.16666, -2.999, 5.555, -7.123])

print("np.trunc:", np.trunc(arr))
print("np.fix:", np.fix(arr))
print("np.around (1 decimal):", np.around(arr, decimals=1))
print("np.floor:", np.floor(arr))
print("np.ceil:", np.ceil(arr))

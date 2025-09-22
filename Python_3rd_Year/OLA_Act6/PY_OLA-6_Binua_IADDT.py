print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# Iterating Array with Different Data Types

import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr,
flags=['buffered'], op_dtypes=['S']):
 print(x)
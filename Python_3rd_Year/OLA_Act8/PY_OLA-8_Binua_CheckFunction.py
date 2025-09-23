print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# Check if a Function is a ufunc

import numpy as np
print(type(np.add))
if type(np.add) == np.ufunc:
 print('add is ufunc')
else:
 print('add is not ufunc')
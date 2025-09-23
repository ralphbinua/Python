print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# Log Base

import numpy as np
import math
arr = np.arange(1, 10)
log_base = 3
print("Log at Base 2:", np.log2(arr))
print("Log at Base 10:", np.log10(arr))
print("Log at Base e:", np.log(arr))
log_func = np.frompyfunc(lambda x, base: math.log(x, base), 2, 1)
print("Log base 3:", log_func(arr, log_base))
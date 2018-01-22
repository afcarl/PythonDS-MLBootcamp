# NumPy Operations

import numpy as np

arr = np.arange(0,11)
arr

arr + arr
arr - arr
arr * arr
arr * 4

# Throws a nan warning as we are trying to divide by "0"
arr / arr

# here you get an "inf" or "infinity" warning
1/arr


# Universal Array functions

np.sqrt(arr)
np.exp(arr)

# The following produce the same result
np.max(arr)
arr.max()

# again throws an error for trying to grab the log of "0" and shows "-inf" or negative infinity
np.log(arr)

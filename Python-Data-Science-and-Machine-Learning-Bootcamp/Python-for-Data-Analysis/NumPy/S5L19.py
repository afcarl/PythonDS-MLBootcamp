# Note S5L18 was simply a note correction, it contained no lecture material so it was skipped.

# NumPy - Indexing and Selection

import numpy as np

arr = np.arange(0,11)

# Just like python lists, this will return the indexes from 1 through 4
arr[1:5]

# This returns indexes [0,6)
arr[:6]

# Broadcasting changes all of the values at the given index to '100'

arr[0:5] = 100
arr
arr = np.arange(0,11)


slices_of_arr = arr[0:6]

# When broadcasting over a slice of an array, it will also change the original
slices_of_arr[:] = 99
slices_of_arr
arr

# This is the only way to copy an array without affecting the values of the original array
arr_copy = arr.copy()
arr_copy

# Indexing a Matrix

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
arr_2d
# To grab the value "5"

arr_2d[0][0]

# This grabs the first row
arr_2d[0]

# This also grabs "5"
arr_2d[0,0]
# This grabs "30"
arr_2d[1,2]

# Grabbing sections of the Matrix

# This grabs rows 1 & 2 and Columns 1 & 2
arr_2d[:2,1:]

# This grabs every column of the bottom two rows
arr_2d[1:, :]

# Conditional Selection

arr = np.arange(1,11)
# This returns a boolean array (an array of only boolean values)
bool_arr = arr > 5

# This returns all of the true values of bool_arr
arr[bool_arr]

# Properly done in one step
arr[arr>5]

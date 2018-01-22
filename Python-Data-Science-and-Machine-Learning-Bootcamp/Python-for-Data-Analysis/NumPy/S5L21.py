# NumPy Excerises Overview

import numpy as np

#create an array of 10 0's

np.zeros([1,10])
np.ones([1,10])

#Create an array of 10 5's

arr = np.zeros([1,10])
arr[:] = 5

# Create an array of ints from 10 through 50
np.arange(10,51)

#create an array of all even ints from 10 through 50

np.arange(10,51,2)

# create a 3x3 with values ranging 0-8

np.arange(0,9).reshape(3,3)

# create a 3x3 identity Matrix

np.identity(3)

# use NumPy to generate a random int from 0,1
np.random.randint(0,2)

np.random.randn(1,25)

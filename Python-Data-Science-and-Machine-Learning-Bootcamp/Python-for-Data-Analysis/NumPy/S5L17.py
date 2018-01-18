import numpy as np
# NumPy Arrays


my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

# np.arange similar to range

# prints an array of all even numbers from 0 through 10
print(np.arange(0,11,2))

# print a 5x5 matrix with 0's as values
print(np.zeros((5,5)))

# print a 5x5 matrix with 0's as values
print(np.ones((5,5)))

# lin space

#gives you a one dimensional array with 10 evenly spaced values from 0 through 5
print(np.linspace(0,5,100))

# eye() creates a Identity matrix
print(np.eye(4))

# Create arrays with random numbers

#gives you a 5x5 matrix with random values
print(np.random.rand(5,5))

# gives you a a 4x4 matrix with a gaussian distribution curve
print(np.random.randn(4,4))

# gives you an array of 10 random integers ranging on [0,100)
print(np.random.randint(1,100,10))


arr = np.arange(25)

ranarr = np.random.randint(0,50,10)

# reshape() transforms arrays into multi-dim arrays, must use exact number of elements
arr.reshape(5,5)

ranarr
ranarr.max()
ranarr.min()
# returns the index of the largest value in the array
ranarr.argmax()
ranarr.argmin()


arr = arr.reshape(5,5)
arr.shape()

arr.dtype()

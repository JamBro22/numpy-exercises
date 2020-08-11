import numpy as np

a = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])

# print the dimensions of an array
print(a.ndim)


# print the byte size of an element
print(a.itemsize)


# get datatype
print(a.dtype)

# get the size/no. of elements in an array
print(a.size)

# get the shape of an array (rows, columns) / amount of dimensions and number of elements in those dimensions
print(a.shape)

# getting elements and slicing in a multidimensional array
print(a[0, 2])
# get from all dimensions / change first number to adjust from which dimension to start at
print(a[0:, 2])
# to avoid printing from later dimensions add a number after the colon
print(a[0:2, 2])

# reshape: change the amount of rows and/columns
# print(a)
# a = a.reshape(3, 2)
# print(a)

# print 5 values that are equally spaced between 1 and 3
b = np.linspace(1, 3, 5)
print(b)

c = np.array([1, 2, 3])
# find max value in array
print(np.max(c))

# find min value in array
print(np.min(c))

# calculate the sum of an array
print(np.sum(c))

# axis 0 is columns, axis 1 is rows
print(a.sum(axis=0))
print(a.sum(axis=1))

# get the square root of each element in an array
print(np.sqrt(c))

# get the standard deviation of an array
print(np.std(c))

d = np.array([1, 2, 3])
e = np.array([1, 2, 3])
# math operations for two arrays' elements
print(d+e)
print(d-e)
print(d/e)
print(d*e)

# stacking arrays vertically
print(np.vstack((d, e)))
print(np.hstack((d, e)))

# converting a multidimensional array into a single dimension
print(np.ravel(a))

# exponential function
print(np.exp(d))

# logarithmic function: log base e
print(np.log(d))

# logarithmic function: log base 10
print(np.log10(d))

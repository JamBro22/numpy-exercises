import numpy as np

# creating a test array
anArray = [1, 2, 3, 4, 5]


# a function returning the mean of an array
def mean(arr):
    return np.mean(arr)


# function returning the standard deviation of an array of numbers
def standard_deviation(arr):
    return np.std(arr)


# a function returning the variance of an array of numbers
def variance(arr):
    return np.var(arr)


# printing results
print(mean(anArray))
print(standard_deviation(anArray))
print(variance(anArray))


# Write a NumPy program to compute the mean, standard deviation,
# and variance of a given array along the second axis. Use np.arange function to generate
# 20 numbers starting from 0

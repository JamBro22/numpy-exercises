# import modules
import matplotlib.pyplot as plt
import numpy as np

# create numpy arrays
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

# print output
print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))

# creating axes labels and title
plt.xlabel("nums")
plt.ylabel("bins")
plt.title("Histogram of nums against bins")
# create matplotlib histogram
plt.hist(nums, bins=bins)
# display histogram
plt.show()


# Write a NumPy program to compute the histogram of nums against the bins. Label your x-axis with nums and y-axis with
# bins.
# Add a title to the histogram: Histogram of nums against bins.
# Sample Output:
# nums: [0.5 0.7 1. 1.2 1.3 2.1]
# bins: [0 1 2 3]
# Result: (array([2, 3, 1], dtype=int64), array([0, 1, 2, 3]))

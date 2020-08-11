import numpy as np
import matplotlib.pyplot as plt


# plotting a cos graph
x = np.arange(0, 3*np.pi, 0.1)

y = np.cos(x)

plt.plot(x, y)

plt.show()

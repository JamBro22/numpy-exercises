import numpy as np
import matplotlib.pyplot as plt

# plotting a sin graph
x = np.arange(0, 3*np.pi, 0.1)

y = np.sin(x)

plt.plot(x, y)

plt.show()

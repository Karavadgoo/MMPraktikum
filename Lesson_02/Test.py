import numpy as np

N = 1000000
X = np.random.uniform(0, 1, size=(N, 2))
inside = np.sum(X**2, axis=1) < 1
area = np.mean(inside)

print(area)
print(np.pi / 4)

v = np.cumsum(inside) / np.arange(1, N+1)
err = np.abs(v - np.pi / 4)

from matplotlib import pyplot

pyplot.plot(err)
pyplot.xlabel('Iteration')
pyplot.ylabel('Absolute deviation')
pyplot.show()
import numpy as np
import matplotlib.pyplot as plt

N = 1000000
x = np.random.rand(N)
nbins = 20
count, bins, patches = plt.hist(x, nbins, density=1)

plt.xlabel("value")
plt.ylabel('probability density')
plt.title('Uniform distribution PDF')
y = np.ones_like(bins)
plt.plot(bins,y,linewidth = 4)
plt.show()
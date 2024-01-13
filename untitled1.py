import numpy as np
import matplotlib.pyplot as plt

N = 1000000
x = np.random.randn(N)
#print(x)

nbins = 1000
count, bins, patches = plt.hist(x, nbins, density=1)

y =(1/np.sqrt(2*np.pi)) * np.exp(-(bins**2)/2)
plt.plot(bins,y,linewidth = 4)
plt.xlabel('x')
plt.ylabel('f_X(x)')
plt.grid()
plt.title('Gaussian PDF')
plt.show()

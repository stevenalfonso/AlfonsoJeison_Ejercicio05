import numpy as npb
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

f = open("coin.txt", "r")
data = f.read()

def vero(data, H):
    Nc = 0
    Ns = 0
    for i in data:
        if i == 'c':
            Nc = Nc + 1
        else:
            Ns = Ns + 1
    return H**Nc *(1 - H)**Ns

H = np.linspace(0,1,100)
L = vero(data, H)

Lmax = np.argmax(L)
H0 = H[Lmax]
sigma = np.sqrt(H0*(1-H0)/len(H))

plt.plot(H, L)
plt.plot(H, stats.norm.pdf(H, H0, sigma),label='Fit')
plt.xlabel("H")
plt.ylabel(r'P(H|obs)')
plt.legend()
plt.title(r'$H = $ %0.4f' %H0 + r'$\pm$ %0.4f' %sigma)
plt.savefig('coin.png')
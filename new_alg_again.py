import numpy as np
from scipy.ndimage.measurements import label
import time
import matplotlib.pyplot as plt


def randarr(p,n):
    b = np.random.binomial(1,p,size=(n,n))
    return b

def randarr_lab(p,n):
    b = np.random.binomial(1,p,size=(n,n))
    a = label(b)[0]
    return a

def percol_iter(n,p):
    cout =0
    for k in range(10000):
        a  = randarr_lab(p,n)
        chek = np.intersect1d(a[0],a[-1])
        if any([x >0 for x in chek]):
            cout = cout + 1
    return cout/10000

p = np.linspace(0,1,100)
c = np.linspace(0,1,100)

for i in range(p.shape[0]):
    c[i] = percol_iter(10,p[i])
    print(i)

plt.plot(p,c)
plt.show()

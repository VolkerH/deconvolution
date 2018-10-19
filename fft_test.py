'''
test fft
'''

import numpy as np
import timeit

def DFT_slow(x):
    '''computer the discrete Fourier Transform of the 1D array x
    '''
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j*np.pi* k*n/N)
    return np.dot(M,x)

x = np.random.random(1024)
print(np.allclose(DFT_slow(x), np.fft.fft(x)))
timeit.timeit(DFT_slow(x))
#print(%timeit.timeit(np.fft.fft(x)))

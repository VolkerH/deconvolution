"""
bessel function
from https://docs.scipy.org/doc/scipy/reference/tutorial/special.html
"""

from scipy import special
import matplotlib.pyplot as plt
from mpl_toolkets.mplot3d import Axes3D
from matplotlib import cm



def drumhead_height(n, k, distance, angle, t):
    kth_zero = special.jn_zeros(n, k)[-1]
    return np.cos(t) * np.cos(n*angle) * special.jn(n, distance * kth_zero)

theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r*])

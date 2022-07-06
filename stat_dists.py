# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:30:04 2022

@author: p4u1
"""

from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

n, p = 100, 0.8

mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')

print(mean,var,skew,kurt)

print(n*(1-p)*p)

x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
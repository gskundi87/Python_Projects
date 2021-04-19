# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:19:52 2021

@author: p4ul
"""

import scipy.stats as sst
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
x = np.linspace(sst.t.ppf(0.01,5),sst.t.ppf(0.99,5),100)
x1 = np.linspace(sst.t.ppf(0.01,50),sst.t.ppf(0.99,50),100)

ax.plot(x, sst.t.pdf(x, 5))
ax.plot(x1, sst.t.pdf(x1, 50))
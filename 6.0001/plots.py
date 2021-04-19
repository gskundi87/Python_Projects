# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:29:32 2020

@author: p4u1
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,30,num=31)

myQuadratic = []
myCube = []

for i in x:
    myQuadratic.append(i**2)
    myCube.append(i**3)

plt.scatter(x,myQuadratic)
plt.scatter(x,myCube)
plt.show()




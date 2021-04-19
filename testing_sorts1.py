# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:10:49 2021

@author: p4ul
"""


import timeit

setup1 = '''
import numpy as np
import sorts

rng = np.random.default_rng()
s = 20*rng.random(10000000) - 10

b_sort = sorts.quicksort
'''

print((timeit.Timer('a=s[:]; b_sort(a,0,len(a)-1)', setup=setup1).repeat(1, 1)))

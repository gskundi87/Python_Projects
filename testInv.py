# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:11:03 2021

@author: p4ul
"""

from sorts import *

A = rng.integers(-10000,10000,1000)

B = A.copy()

C = A.copy()

x = count_inv(B)

print(x)

print(insertion_sort_count_inv(C))
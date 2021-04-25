# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:29:54 2021

@author: p4u1
"""

import math
import numpy as np

def findMedian(A,lA,rA,B,lB,rB):
    if lA == rA:
        return A[lA]
    
    if lB == rB:
        return B[lB]
    
    medIndexA = (lA+rA)//2
    medIndexB = (lB+rB)//2
    
    if A[medIndexA] < B[medIndexB]:
        return findMedian(A,medIndexA+1,rA,B,lB,medIndexB)
    else:
        return findMedian(A,lA,medIndexA,B,medIndexB+1,rB)
    
rng = np.random.default_rng()
A = rng.integers(-1000,1000,10)
B = rng.integers(-1000,1000,10)

A = sorted(A)
B = sorted(B)

C = findMedian(A,0,len(A)-1,B,0,len(B)-1)
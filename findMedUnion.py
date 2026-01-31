# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:29:54 2021

@author: p4u1
"""

import math
import numpy as np

rng = np.random.default_rng()
A = rng.integers(-1000,1000,12)
B = rng.integers(-1000,1000,12)

A = list(A)
B = list(B)
D = A+B

A = sorted(A)
B = sorted(B)
D = sorted(D)

E = (D[len(D)//2-1]+D[len(D)//2])/2

def findMedian(A,al,ah,B,bl,bh):
    lengthA = (ah - al + 1)
    lengthB = (bh - bl + 1)
    assert(lengthA == lengthB)
    
    if lengthA == 2:
        C = A[al:ah+1] + B[bl:bh+1]
        C = sorted(C)
        return (C[1] + C[2])/2
    
    pivotA = (al + ah)//2
    pivotB = (bl + bh)//2
    
    if lengthA % 2 == 0:
        medianA = (A[pivotA]+A[pivotA + 1])/2
        medianB = (B[pivotB]+B[pivotB + 1])/2
        
        if medianA > medianB:
            return findMedian(A,al,pivotA+1,B,pivotB,bh)
        else:
            return findMedian(A,pivotA,ah,B,bl,pivotB+1)
    else:
        medianA = A[pivotA]
        medianB = B[pivotB]
        
        if medianA > medianB:
            return findMedian(A,al,pivotA,B,pivotB,bh)
        else:
            return findMedian(A,pivotA,ah,B,bl,pivotB)  

C = findMedian(A,0,len(A)-1,B,0,len(B)-1)
print(f"Brute Force: {E}")
print(f"DC: {C}")
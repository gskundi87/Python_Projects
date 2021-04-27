# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:29:54 2021

@author: p4u1
"""

import math
import numpy as np

rng = np.random.default_rng()
A = rng.integers(-1000,1000,10)
B = rng.integers(-1000,1000,10)

A = list(A)
B = list(B)
D = A+B

A = sorted(A)
B = sorted(B)
D = sorted(D)

E = (D[len(D)//2-1]+D[len(D)//2])/2

def findMedian(A,B):    
    if len(A) == 2:
        C = A + B
        C = sorted(C)
        return (C[1] + C[2])/2
            
    if len(A) % 2 == 0:
        medianA = (A[len(A)//2-1]+A[len(A)//2])/2
        medianB = (B[len(B)//2-1]+B[len(B)//2])/2
        
        if medianA > medianB:
            return findMedian(A[0:len(A)//2+1],B[len(B)//2-1:len(B)+1])
        else:
            return findMedian(A[len(A)//2-1:len(A)+1],B[0:len(B)//2+1])
    else:
        medianA = A[len(A)//2]
        medianB = B[len(B)//2]
        
        if medianA > medianB:
            return findMedian(A[0:len(A)//2+1],B[len(B)//2:len(B)+1])
        else:
            return findMedian(A[len(A)//2:len(A)+1],B[0:len(B)//2+1])  

C = findMedian(A,B)
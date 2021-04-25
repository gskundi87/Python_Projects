# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:29:54 2021

@author: p4u1
"""

import math
import numpy as np

count = 0

def findMedian(A,B):
    if A[len(A)-1] < B[0]:
        return (A[len(A)-1]+B[0])/2
    
    if B[len(B)-1] < A[0]:
        return (B[len(B)-1]+A[0])/2
    
    if len(A) == 2:
        if A[0] > B[0] and A[1] < B[1]:
            return (A[0]+A[1])/2
        elif B[0] > A[0] and B[1] < A[1]:
            return (B[0]+B[1])/2
        elif A[1] < B[0]:
            return (A[1]+B[0])/2
        else:
            return (A[0]+B[1])/2
            
    if len(A) % 2 == 0:
        medianA = (A[len(A)//2-1]+A[len(A)//2])/2
        medianB = (B[len(B)//2-1]+B[len(B)//2])/2
        
        if medianA == medianB:
            return medianA
        elif medianA > medianB:
            return findMedian(A[0:len(A)//2+1],B[len(B)//2-1:len(B)])
        else:
            return findMedian(A[len(A)//2-1:len(A)],B[0:len(B)//2+1])
    else:
        medianA = A[len(A)//2]
        medianB = B[len(B)//2]
        
        if medianA > medianB:
            return findMedian(A[0:len(A)//2+1],B[len(B)//2:len(B)])
        else:
            return findMedian(A[len(A)//2:len(A)],B[0:len(B)//2+1])

# def findMedian(A,lA,rA,B,lB,rB):
#     if lA == rA:
#         return A[lA]
    
#     if lB == rB:
#         return B[lB]
    
#     medIndexA = (lA+rA)//2
#     medIndexB = (lB+rB)//2
    
#     if A[medIndexA] < B[medIndexB]:
#         return findMedian(A,medIndexA,rA,B,lB,medIndexB)
#     else:
#         return findMedian(A,lA,medIndexA,B,medIndexB,rB)
    
rng = np.random.default_rng()
A = rng.integers(-1000000000,1000000000,10000)
B = rng.integers(-1000000000,1000000000,10000)

A = sorted(A)
B = sorted(B)

C = findMedian(A,B)
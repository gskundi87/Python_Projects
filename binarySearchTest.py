# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:27:24 2021

@author: p4ul
"""

import numpy as np
import time

rng = np.random.default_rng()

L = rng.integers(-100000,10000,10000000)
L = sorted(L)
e = rng.integers(-100000,100000,1)

def bSearch1(L, e, low, high):
    if high == low:
        if L[low] == e:
            print(low,e)
            return True
    mid = (low + high)//2
    if L[mid] == e:
        print(mid,e)
        return True
    elif L[mid] > e:
        if low == mid: #nothing left to search
            return False
        else:
            return bSearch1(L, e, low, mid - 1)
    else:
        return bSearch1(L, e, mid + 1, high)
    
def bSearch2(L,e):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0] == e
    mid = len(L)//2
    if L[mid] == e:
        print(L[mid])
        return True
    elif L[mid] > e:
        return bSearch2(L[0:mid],e)
    else:
        return bSearch2(L[mid+1:len(L)],e)
    
time1 = time.perf_counter()
bSearch1(L,e,0,len(L)-1)
time2 = time.perf_counter()
print(f"{time2 - time1:0.4f} seconds") 

time1 = time.perf_counter()
bSearch2(L,e)
time2 = time.perf_counter()
print(f"{time2 - time1:0.4f} seconds") 
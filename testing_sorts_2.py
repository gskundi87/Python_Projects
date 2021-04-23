# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:10:49 2021

@author: p4ul
"""

import time
import numpy as np
from sorts import *
from exponentiation import *

# x = 4587876
# y = 79098987987
# z = 2378

# print(fast_mod_exp_iter(x,y,z))

# print(fast_mod_exp_rec(x,y,z))

# time1 = time.perf_counter()
# fast_mod_exp_iter(x,x,z)
# time2 = time.perf_counter()  
# print(f"Mod Exp Iter in {time2 - time1:0.4f} seconds")

# time1 = time.perf_counter()
# fast_mod_exp_rec(x,y,z)
# time2 = time.perf_counter()  
# print(f"Mod Exp Rec in {time2 - time1:0.4f} seconds")

# print(fast_mult_rec(x,y))

# print(fast_mult_iter(x,y))

# time1 = time.perf_counter()
# fast_mult_iter(x,y)
# time2 = time.perf_counter()  
# print(f"Mult Iter in {time2 - time1:0.4f} seconds")

# time1 = time.perf_counter()
# fast_mult_rec(x,y)
# time2 = time.perf_counter()  
# print(f"Mult Rec in {time2 - time1:0.4f} seconds")

rng = np.random.default_rng()
i1 = 13
i2 = 14

for x in range(i1,i2):
    a = rng.integers(-2**x, 2**x, 2**x)
    b = a.copy()
    c = a.copy()
    
    time1 = time.perf_counter()
    quicksort(a,0,len(a)-1)
    time2 = time.perf_counter()  
    print(f"Quick Sorted in {time2 - time1:0.4f} seconds")
    
    time1 = time.perf_counter()
    random_quicksort(b,0,len(b)-1)
    time2 = time.perf_counter()  
    print(f"Random Quick Sorted in {time2 - time1:0.4f} seconds")
    
    time1 = time.perf_counter()
    det_quicksort(c,0,len(c)-1)
    time2 = time.perf_counter()  
    print(f"Det Quick Sorted in {time2 - time1:0.4f} seconds")
        
    # time1 = time.perf_counter()
    # print(f"{bubble_sort_count_inv(a)} inversions")
    # time2 = time.perf_counter()  
    # print(f"Bubble Sorted in {time2 - time1:0.4f} seconds")
    
    # time1 = time.perf_counter()
    # print(f"{insertion_sort_count_inv(b)} inversions")
    # time2 = time.perf_counter()  
    # print(f"Insertion Sorted in {time2 - time1:0.4f} seconds")
    
    # time1 = time.perf_counter()
    # print(f"{count_inv(c)} inversions")
    # time2 = time.perf_counter()  
    # print(f"Count Inversions in {time2 - time1:0.4f} seconds")
        
    # for x in range(i1,i2):
    #     a = rng.integers(-2**x, 2**x, 2**x)
    #     time1 = time.perf_counter()
    #     print(insertion_sort_count_inv(a))
    #     time2 = time.perf_counter()  
    #     print(f"Insertion Sorted in {time2 - time1:0.4f} seconds")
        
    # for x in range(i1,i2):
    #     a = rng.integers(-2**x, 2**x, 2**x)
    #     b = heap(a)
    #     time1 = time.perf_counter()
    #     b.heapsort()
    #     time2 = time.perf_counter()  
    #     print(f"Heap Sorted in {time2 - time1:0.4f} seconds")
    
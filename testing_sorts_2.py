# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:10:49 2021

@author: p4ul
"""

import time
import numpy as np
from sorts import *

def main():
    rng = np.random.default_rng()
    i1 = 16
    i2 = 18
    
    # for x in range(5,14):
    #     a = rng.integers(-2**x, 2**x, 2**x)
    #     time1 = time.perf_counter()
    #     selection_sort(a)
    #     time2 = time.perf_counter()  
    #     print(f"Selection Sorted in {time2 - time1:0.4f} seconds")
        
    # for x in range(5,14):
    #     a = rng.integers(-2**x, 2**x, 2**x)
    #     time1 = time.perf_counter()
    #     insertion_sort(a)
    #     time2 = time.perf_counter()  
    #     print(f"Insertion Sorted in {time2 - time1:0.4f} seconds")
        
    for x in range(i1,i2):
        a = rng.integers(-2**x, 2**x, 2**x)
        b = heap(a)
        time1 = time.perf_counter()
        b.heapsort()
        time2 = time.perf_counter()  
        print(f"Heap Sorted in {time2 - time1:0.4f} seconds")
        
    for x in range(i1,i2):
        a = rng.integers(-2**x, 2**x, 2**x)
        time1 = time.perf_counter()
        quicksort(a,0,len(a)-1)
        time2 = time.perf_counter()  
        print(f"Quick Sorted in {time2 - time1:0.4f} seconds")
        
    for x in range(i1,i2):
        a = rng.integers(-2**x, 2**x, 2**x)
        time1 = time.perf_counter()
        random_quicksort(a,0,len(a)-1)
        time2 = time.perf_counter()  
        print(f"Random Quick Sorted in {time2 - time1:0.4f} seconds")
    
if __name__ == "__main__":
    main()
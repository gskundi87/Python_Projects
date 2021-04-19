# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:00:19 2021

@author: p4ul
"""

from timer import Timer
import numpy as np
import sorts


def main():
    rng = np.random.default_rng()
    A = rng.integers(-1000000,1000000,10000)
    B = A.copy()
    
    t = Timer(name = "class")
    t.start()
    sorts.quicksort(A,0,len(A)-1)
    t.stop()
    
    A = rng.integers(-1000000,1000000,10000)
    t.start()
    sorts.bubble_sort(B)
    t.stop()

if __name__ == "__main__":
    main()
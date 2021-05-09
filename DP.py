# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:03:06 2021

@author: p4u1
"""

import time

def fib_rec(x):
    if x == 0 or x == 1:
        return x
    
    else:
        return fib_rec(x-2) + fib_rec(x-1)
    
memo_1 = {0:0, 1:1}
    
def fib_dyn_1(x):
    global memo_1
    
    if x in memo_1:
        return memo_1[x]
    
    memo_1[x] = fib_dyn_1(x-2) + fib_dyn_1(x-1)
    return memo_1[x]

def fib_dyn_2(x):
    fib = [0,1]
    
    if x == 0 or x == 1:
        return x
    
    for i in range(2,x+1):
        n = fib[i-2] + fib[i-1]
        fib.append(n)
        
    return fib[x]

x = 1000

# time1 = time.perf_counter()
# print(fib_rec(x))
# time2 = time.perf_counter()  
# print(f"Fib_rec {x} in {time2 - time1:0.4f} seconds")

time1 = time.perf_counter()
print(fib_dyn_1(x))
time2 = time.perf_counter()  
print(f"Fib_dyn_1 {x} in {time2 - time1:0.4f} seconds")

time1 = time.perf_counter()
print(fib_dyn_2(x))
time2 = time.perf_counter()  
print(f"Fib_dyn_2 {x} in {time2 - time1:0.4f} seconds")


        
    
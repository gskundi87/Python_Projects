# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:49:57 2020

@author: p4u1
"""

import random

# a = random.sample(range(-25,25),25)

def fast_exp_rec(x,y):
    if y == 0:
        return 1
    
    y1 = y // 2
    
    z = fast_exp_rec(x,y1)
    
    if y % 2 == 0:
        return z*z
    elif y % 2 == 1:
        return z*z*x
    
def fast_exp_iter(x,y):
    result = 1
    power = x
    exp = y
    
    while exp > 0:
        if exp % 2 == 1:
            result = result*power
        power = power*power
        exp = exp // 2
        
    return result

def fast_mod_exp_rec(x,y,m):
    if x == 0:
        return 0
    if y == 0:
        return 1
     
    z = 0
    
    if (y % 2) == 0:
        z = fast_mod_exp_rec(x,y//2,m)
        z = (z*z) % m
    else:
        z = x % m
        z = (z*fast_mod_exp_rec(x,y-1,m) % m) % m
    return ((z+m) % m)

def fast_mod_exp_iter(x,y,m):
    result = 1
    power = x
    exp = y
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result*power) % m
        power = (power*power) % m
        exp = exp // 2
        
    return result
    
def fast_mult_rec(x,y):
    if x == 0 or y == 0:
        return 0
    
    y1 = y // 2
    
    z = fast_mult_rec(x,y1)
    
    if y % 2 == 0:
        return 2*z
    elif y % 2 == 1:
        return 2*z + x
    
def fast_mult_iter(x,y):
    result = 0
    power = 1
    multiplier = y
    
    while multiplier > 0:
        if multiplier % 2 == 1:
            result += x*power
        power *= 2
        multiplier = multiplier//2
        
    return result

def gcd(a,b):
    while b != 0:
        temp = a
        a = b
        b = temp % b 
    return a

# print(gcd(662,414))

# print(fast_exp_rec(4,4))

# print(fast_mod_exp_iter(3,13,7))

# print(mod_exp(3,13,7))

# print(fast_exp_iter(4,4))

# print(fast_mult_rec(5467,3456))

# print(fast_mult_iter(5467,3456))

# a = insertion_sort_iter(a)
    
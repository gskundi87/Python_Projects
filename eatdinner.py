# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:14:12 2021

@author: p4u1
"""

free = [1,0,1,1,0,0,0,1,0,0,1,1,1,0,0]

def Eat(n):
    global free
    
    if n < 0:
        return 0
    if free[n] == 1:
        return Eat(n-1)
    
    cafeteria = 6 + Eat(n-1)
    
    groceries = 20 + Eat(n-7)
        
    return min(cafeteria,groceries)

print(Eat(13))


# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:06:39 2021

@author: p4ul
"""

import random
import math

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]

def find_median(B):
    if len(B) <= 5:
        bubble_sort(B)
        return B[len(B)//2]
    g = math.ceil(len(B)//5)
    temp = [0] * g
    for x in range(0,g):
        C = B[5*x:5*(x+1)]
        temp[x] = find_median(C)
    return find_median(temp)
    
def linear_search(A,x):
    for i in range(0,len(A)):
        if A[i] == x:
            return i
    return -1

def make_set(count, maximum):
    A = []
    
    for i in range(0,count):
        a = random.randint(0, maximum)
        b = random.randint(0, maximum)
        c = (a,b)
        A.append(c)
        
    return A

def minima_set_BF(A):
    B = []
    for i in range(0,len(A)):
        flag = True
        for j in range(0,len(A)):
            if i != j:             
                if A[i][0] > A[j][0] and A[i][1] < A[j][1]:
                    flag = False
                    break            
        if flag:
            B.append(A[i])
    return B

def minima_set_DC(A):
    return

A = [(4,65),(8,15),(8.5,2),(2,35),(10,0),(9,85),(8.2,90)]

B = minima_set_BF(A)

print(B)
        
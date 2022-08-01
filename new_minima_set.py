# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:06:39 2021

@author: p4ul
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(x,p,r):
    for i in range(0,r-p):
        for j in range(p,r-i):
            if x[j][0] > x[j+1][0]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

def find_median(B,p,r):
    if r-p+1 <= 5:
        B = bubble_sort(B,p,r)
        return B[(p+r)//2]
    g = ((r-p)//5)
    temp = []
    end = 0
    for x in range(0,g):
        start = 5*x
        end = 5*(x+1)-1
        temp.append(find_median(B,start,end))
    temp.append(find_median(B,end+1,len(B)-1))
    return find_median(temp,0,len(temp)-1)

def find_min(A):
    minimum = A[0]
    for i in range(1,len(A)):
        if A[i][1] < minimum[1]:
            minimum = A[i]
    return minimum

def make_set(count, maximum1, maximum2):
    A = []
    
    for i in range(0,count):
        a = random.randint(0, maximum1)
        b = random.randint(0, maximum2)
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
    if len(A) <= 5:
        return minima_set_BF(A)
    p = find_median(A,0,len(A)-1)
    L = [x for x in A if x[0] <= p[0]]
    G = [x for x in A if x[0] > p[0]]
    M1 = minima_set_DC(L)
    M2 = minima_set_DC(G)
    m = find_min(M1)
    temp = []
    for m2 in M2:
        if m2[1] < m[1]:
            temp.append(m2)
    return list(M1 + temp)  

# A = [(4,65),(8,15),(8.5,2),(2,35),(10,0),(9,85),(8.2,90)]

A = make_set(10,10,100)
D = A.copy()

points = np.array(A)

x,y = points.T

plt.scatter(x,y)
plt.show()

B = minima_set_BF(A)
C = minima_set_DC(D)

print(B)
print(C)
        
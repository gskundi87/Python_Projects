# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:41:06 2021

@author: p4u1
"""
n = 5
p = [0.1, 0.2, 0.05, 0.15, 0.5]

X = [[0 for x in range(n)] for y in range(n)] 

print(X)

for i in range(0,n):
    X[i][i] = p[i]
    
for i in range(0,n):
    for j in range(i+1,n):
        X[i][j] = X[j][i] = X[i][j-1] + p[j]
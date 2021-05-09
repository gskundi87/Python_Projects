# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:00:19 2021

@author: p4u1
"""

def partition(A,p,r):
    x = A[r][1]
    i = p - 1
    
    for j in range(p,r):
        if A[j][1] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
            
    A[i+1],A[r] = A[r],A[i+1]
    
    return i + 1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
        
intervals = [(9,12,1),(5,7,4),(3,10,7),(2,6,4),(1,4,2),(8,11,2)]

quicksort(intervals,0,len(intervals)-1)

record = [-1]*len(intervals)

def binarySearch(p,s,e,i,v):
    global record
    x = (s+e)//2
    if p[x][1] < v:
        if record[i] == -1 or p[x][1] > p[record[i]][1]:
            record[i] = x
        if s >= e:
            return
        binarySearch(p,x+1,e,i,v)
    else:
        if s >= e:
            return
        binarySearch(p,s,x-1,i,v)

for i in range(0,len(intervals)):
    binarySearch(intervals,0,len(intervals)-1,i,intervals[i][0])
    
memo = [[0,False]]

def opt(i):
    global memo
    global intervals
    global record
    
    x = memo[i-1][0]
    
    if record[i-1] == -1:
        z = 0
    else:
        z = memo[record[i-1]+1][0]
    
    y = intervals[i-1][2] + z
    
    if x > y:
        memo.append([x,False])
    else:
        memo.append([y,False])
        
for i in range(1,len(intervals)+1):
    opt(i)

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:54:58 2021

@author: p4ul
"""
import numpy as np
import math
import random

# rng = np.random.default_rng()

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

def bubble_sort_count_inv(x):
    count = 0
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                count = count + 1
                x[j],x[j+1] = x[j+1],x[j]
    return count

def selection_sort(x):
    for i in range(len(x)-1):
        index = i
        for j in range(i+1,len(x)):
            if x[index] > x[j]:
                index = j
        x[i],x[index] = x[index],x[i]       

def insertion_sort(x):
    for i in range(1,len(x)):
        key = x[i]
        index = i - 1
        
        while index >= 0 and x[index] > key:
            x[index+1] = x[index]
            index = index - 1
            
        x[index+1] = key
        
def insertion_sort_count_inv(x):
    count = 0
    for i in range(1,len(x)):
        key = x[i]
        index = i - 1
        
        while index >= 0 and x[index] > key:
            count = count + 1
            x[index+1] = x[index]
            index = index- 1
            
        x[index+1] = key
        
    return count

class heap(object):
    def __init__(self, list):
        self.list = list.copy()
        self.heapSize = 0
        
    def isEmpty(self):
        if len(list) == 0:
            return True
        else:
            return False
        
    def parent(self, index):
        return (index - 1) // 2
    
    def left(self, index):
        return 2*index + 1
    
    def right(self, index):
        return 2*index + 2
    
    def insert(self, x):
        self.list.append(x)
        
    def getList(self):
        return self.list[:]
        
    def maxHeapify(self, index):
        l = self.left(index)
        r = self.right(index)
        
        if l < self.heapSize and self.list[l] > self.list[index]:
            largest = l
        else:
            largest = index
            
        if r < self.heapSize and self.list[r] > self.list[largest]:
            largest = r
            
        if largest != index:
            self.list[index], self.list[largest] = self.list[largest], self.list[index]
            self.maxHeapify(largest)
            
    def buildMaxHeap(self):
        self.heapSize = len(self.list)
        
        for x in range((len(self.list) - 1) // 2, -1, -1):
            self.maxHeapify(x)
            
    def heapsort(self):
        self.buildMaxHeap()
        
        for x in range(len(self.list) - 1, 0, -1):
            self.list[0], self.list[x] = self.list[x], self.list[0]
            self.heapSize = self.heapSize - 1
            self.maxHeapify(0)
            
    def __str__(self):
        result = ''
        for x in self.list:
            result = result + str(x) + ','
        return '{' + result[:-1] + '}'
    
def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        
def merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    
    i = 0
    j = 0
    k = p
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1
      
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    
    
def merge_and_count(A):
    count = 0
    i = 0
    j = len(A)//2
    temp = [0] * len(A)
    k = 0
    
    while i < len(A)//2 and j < len(A):
        if A[i] < A[j]:
            temp[k] = A[i]
            k += 1
            i += 1
        else:
            temp[k] = A[j]
            k += 1
            count += ((len(A)//2) - i)
            j += 1
            
    while i < len(A)//2:
        temp[k] = A[i]
        k += 1
        i += 1
    
    while j < len(A):
        temp[k] = A[j]
        k += 1
        j += 1
    
    for i in range(0,len(A)):
        A[i] = temp[i]
    
    return count
        
def count_inv(A):
    if len(A) < 10:
        return insertion_sort_count_inv(A)
    
    else:
        L = A[0:len(A)//2]
        R = A[len(A)//2:len(A)]
        
        cL = count_inv(L)
        cR = count_inv(R)
        cM = merge_and_count(A)
        
        return cL + cR + cM
        
def partition(A,p,r):
    x = A[r]
    i = p - 1
    
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
            
    A[i+1],A[r] = A[r],A[i+1]
    
    return i + 1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
        
def random_partition(A,p,r):
    x = random.randint(p,r)
    A[x],A[r] = A[r],A[x]
    return partition(A,p,r)

def random_quicksort(A,p,r):
    if p < r:
        q = random_partition(A,p,r)
        random_quicksort(A,p,q-1)
        random_quicksort(A,q+1,r)

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

def det_partition(A,p,r):
    y = find_median(A[p:r+1])
    x = linear_search(A[p:r+1],y)
    A[x+p],A[r] = A[r],A[x+p]
    return partition(A,p,r)

def det_quicksort(A,p,r):
    if p < r:
        q = det_partition(A,p,r)
        det_quicksort(A,p,q-1)
        det_quicksort(A,q+1,r)

def det_quick_select(A,x):
    if x < 0 or x > len(A):
        return -1
    if len(A) <= 10:
        quicksort(A,0,len(A)-1)
        return A[x-1]
    q = det_partition(A,0,len(A)-1)
    if x == q + 1:
        return A[q]
    if x < q + 1:
        return det_quick_select(A[0:q],x)
    return det_quick_select(A[q+1:len(A)],x-q-1)


                
# A = rng.integers(-1000,1000,50)
# B = A.copy()

# print(det_quick_select(B,50))
# A = bubble_sort(A)

# print(A[49])

# find_median(B)

# det_quicksort(B,0,len(B)-1)
# print(B)

# x = 41
# n = det_quick_select(A,x)
# quicksort(B,0,len(B)-1)
# print(n)
# print(B[x-1])

def tryone(n, tries):
    from random import random
    from time import perf_counter

    x = [None] * n
    median_rank = (n+1) // 2
    sum1 = sum2 = 0.0
    for i in range(tries):
        for i in range(n):
            x[i] = random()
            
        y = x[:]
        start = perf_counter()
        got1 = det_quick_select(x,median_rank)
        elapsed = perf_counter() - start
        sum1 += elapsed

    return sum1, sum2

def trytwo(n, tries):
    from random import random
    from time import perf_counter

    x = [None] * n
    median_rank = (n+1) // 2
    sum1 = sum2 = 0.0
    for i in range(tries):
        for i in range(n):
            x[i] = random()
            
        y = x[:]
        start = perf_counter()
        got1 = insertion_sort_count_inv(x)
        elapsed = perf_counter() - start
        sum1 += elapsed
        start1 = perf_counter()
        got2 = count_inv(y)
        elapsed1 = perf_counter() - start1
        sum2 += elapsed1

    return sum1, sum2, got1, got2

def drive(tries):
    for i in range(10):
        n = 2**i + 1
        fast, slow, got1, got2 = trytwo(n, tries)
        print (f"%8d %7.3f %7.3f %d %d" % (n, fast/tries, slow/tries, got1, got2))

# if __name__ == "__main__":
    #drive(3)
x = []

for i in range(10):
    x.append(random.randint(0,100))

print(x)
merge_sort(x,0,len(x)-1)
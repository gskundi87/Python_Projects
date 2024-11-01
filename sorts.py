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

def bubble_sort_ip(x,p,r):
    for i in range(p,r):
        for j in range(p,r-i):
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
    temp = [None] * len(A)
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
    if len(A) == 1:
        return 0
    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
            return 1
        else:
            return 0
    
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

def find_median(B,p,r):
    lenB = r - p + 1
    if lenB == 1 or lenB == 2:
        return B[p]
    if lenB == 3:
        bubble_sort_ip(B,p,r)
        return B[p+1]
    if lenB == 4 or lenB == 5:
        bubble_sort_ip(B,p,r)
        return B[p+2]
    g = ((len(B)//5) if (len(B) % 5 == 0) else ((len(B)//5) + 1))
    temp = [0] * g
    for x in range(g-1):
        pC = 5*x
        rC = 5*(x+1) - 1
        temp[x] = find_median(B,pC,rC)
    temp[g-1] = find_median(B,5*(g-1),len(B)-1)
    return find_median(temp,0,len(temp)-1)

def find_median_iter(B,p,r):
    lenB = r - p + 1
    if lenB <= 5:
        return get_median_small_list(B,p,r)
    else:
        g = ((lenB//5) if (lenB % 5 == 0) else ((lenB//5) + 1))
        temp = []
        for x in range(g-1):
            i = p+(5*x)
            temp.append(get_median_small_list(B,i,i+4))
        temp.append(get_median_small_list(B,p+(5*(g-1)),r))
        B1 = temp 

        lenB1 = len(B1)
        while(lenB1 > 5):
            g = ((lenB1//5) if (lenB1 % 5 == 0) else ((lenB1//5) + 1))
            temp = []
            for x in range(g-1):
                i = 5*x
                temp.append(get_median_small_list(B1,i,i+4))
            temp.append(get_median_small_list(B1,(5*(g-1)),lenB1-1))
            B1 = temp
            lenB1 = len(B1)
        
        return get_median_small_list(B1,0,lenB1-1)

def get_median_small_list(B,p,r):
    lenB = r - p + 1
    if lenB == 1 or lenB == 2:
        return B[p]
    bubble_sort_ip(B,p,r)
    return B[p+1]
    
    
def linear_search(A,p,r,x):
    for i in range(p,r+1):
        if A[i] == x:
            return i
    return -1

def det_partition(A,p,r):
    y = find_median_iter(A,p,r)
    x = linear_search(A,p,r,y)
    A[x],A[r] = A[r],A[x]
    return partition(A,p,r)

def det_quicksort(A,p,r):
    if p < r:
        q = det_partition(A,p,r)
        det_quicksort(A,p,q-1)
        det_quicksort(A,q+1,r)

def det_quick_select(A,p,r,x):
    if x < 0 or x > len(A):
        return -1
    if len(A) <= 10:
        quicksort(A,0,len(A)-1)
        return A[x-1]
    q = det_partition(A,0,len(A)-1)
    if x == q + 1:
        return A[q]
    if x < q + 1:
        return det_quick_select(A,0,q-1,x)
    return det_quick_select(A,q+1,len(A)-1,x-q-1)

def testSorts(n, tries):
    from time import perf_counter

    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    
    x = []
    
    for i in range(tries):
        for j in range(n):
            x.append(random.randint(0,10*n)) 
        y = x[:]
        start = perf_counter()
        got1 = quicksort(x,0,len(x)-1)
        elapsed = perf_counter() - start
        sum1 += elapsed
        start1 = perf_counter()
        got2 = random_quicksort(y,0,len(y)-1)
        elapsed1 = perf_counter() - start1
        sum2 += elapsed1
        start2 = perf_counter()
        got3 = det_quicksort(y,0,len(y)-1)
        elapsed2 = perf_counter() - start2
        sum3 += elapsed2

    return sum1, sum2, sum3, got1, got2, got3

def driveSortTest(tries):
    for i in range(21,22):
        n = 2**i
        time1, time2, time3, got1, got2, got3 = testSorts(n, tries)
        print (f"%8d, %7.3f, %7.3f %7.3f" % (n,time1/tries,time2/tries,time3/tries))

# Compare quicksort algorithms for simple version and random version
# Looks like asymptotically the random versioin is better
if __name__ == "__main__":
    A = []
    
    for i in range(32):
        A.append(random.randint(0,100))

    B = A.copy()
    C = A.copy()
    
    print(f"A median:  %d", find_median_iter(A,0,len(A)-1))
    print(f"B median:  %d", find_median_iter(B,0,len(B)-1))
    print(f"C median:  %d", find_median_iter(C,0,len(C)-1))
    
    print(A)
    print(B)
    print(C)
    
    quicksort(A,0,len(A)-1)
    random_quicksort(B,0,len(B)-1)
    det_quicksort(C,0,len(C)-1)
    
    print(A)
    print(B)
    print(C)

    driveSortTest(1)

# Test accuracy of count_inv vs simpler inversion counting methods
# Currently not accurate as of 9/19/21 -> TODO
# if __name__ == "__main__":
#     A = []
    
#     for i in range(20):
#         A.append(random.randint(0,100))
    
#     B = A.copy()
#     C = A.copy()
    
#     print(A)
#     print(B)
#     print(C)
    
#     count1 = bubble_sort_count_inv(A)
#     count2 = insertion_sort_count_inv(B)
#     count3 = count_inv(C)
    
#     print(A)
#     print(B)
#     print(C)
    
#     print(count1)
#     print(count2)
#     print(count3)
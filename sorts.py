# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:54:58 2021

@author: p4ul
"""
import numpy as np

rng = np.random.default_rng()

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

def selection_sort(x):
    for i in range(len(x)-1):
        index = i
        for j in range(i+1,len(x)):
            if x[index] > x[j]:
                index = j
        x[i],x[index] = x[index],x[i]       
    return x

def insertion_sort(x):
    for i in range(2,len(x)-1):
        key = x[i]
        index = i - 1
        
        while index >= 0 and x[index] > key:
            x[index+1] = x[index]
            index = index- 1
            
        x[index+1] = key

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
    x = rng.integers(p,r+1,1)
    A[x],A[r] = A[r],A[x]
    return partition(A,p,r)

def random_quicksort(A,p,r):
    if p < r:
        q = random_partition(A,p,r)
        random_quicksort(A,p,q-1)
        random_quicksort(A,q+1,r) 
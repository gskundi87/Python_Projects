# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:19:59 2021

@author: p4u13
"""

vertices_list = [['a',0,False,None],['b',1000000,False,None],['c',1000000,False,None],
            ['d',1000000,False,None],['e',1000000,False,None],['f',1000000,False,None],
            ['g',1000000,False,None],['h',1000000,False,None]]

vertices_dict = {'a': ['a',0,False,None], 'b': ['b',1000000,False,None], 'c': ['c',1000000,False,None],
            'd': ['d',1000000,False,None], 'e': ['e',1000000,False,None], 'f': ['f',1000000,False,None],
            'g': ['g',1000000,False,None], 'h': ['h',1000000,False,None]}



edges = {'a': [('a','b'),('a','c')]}
edges['b'] = [('b','a'),('b','c'),('b','d'),('b','e')]
edges['c'] = [('c','a'),('c','b'),('c','d')]
edges['d'] = [('d','b'),('d','c'),('d','e'),('d','f'),('d','g')]
edges['e'] = [('e','b'),('e','d'),('e','f'),('e','h')]
edges['f'] = [('f','d'),('f','e'),('f','g')]
edges['g'] = [('g','d'),('g','f'),('g','h')]
edges['h'] = [('h','e'),('h','g')]

weights = {('a','b'): 2, ('b','a'): 2}
weights[('a','c')] = 4
weights[('c','a')] = 4
weights[('b','c')] = 1
weights[('c','b')] = 1
weights[('c','d')] = 4
weights[('d','c')] = 4
weights[('b','d')] = 6
weights[('d','b')] = 6
weights[('b','e')] = 5
weights[('e','b')] = 5
weights[('d','e')] = 2
weights[('e','d')] = 2
weights[('d','g')] = 1
weights[('g','d')] = 1
weights[('d','f')] = 2
weights[('f','d')] = 2
weights[('e','f')] = 8
weights[('f','e')] = 8
weights[('f','g')] = 3
weights[('g','f')] = 3
weights[('e','h')] = 2
weights[('h','e')] = 2
weights[('g','h')] = 4
weights[('h','g')] = 4

class heap(list,dict):
    def __init__(self, list):
        self.__list = list.copy()
        self.__dict = dict.copy()
        self.heapSize = 0
        
    def isEmpty(self):
        if len(self.__list) == 0:
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
        
    def extractMin(self):
        if self.isEmpty():
            return None
        else:
            self.__list[0], self.__list[self.heapSize - 1] = \
            self.__list[self.heapSize - 1], self.__list[0]
            self.heapSsize -= 1
            self.minHeapify(0)
            return self.__list[self.heapSize]
        
    def minHeapify(self, index):
        l = self.left(index)
        r = self.right(index)
        
        if l < self.heapSize and self.__list[l][2] < self.__list[index][2]:
            smallest = l
        else:
            smallest = index
            
        if r < self.__heapSize and self.__list[r][2] < self.__list[smallest][2]:
            smallest = r
            
        if smallest != index:
            self.__list[index], self.__list[smallest] = \
            self.__list[smallest], self.__list[index]
            self.minHeapify(smallest)
            
    def buildMinHeap(self):
        self.heapSize = len(self.__list)
        
        for x in range((len(self.__list) - 1) // 2, -1, -1):
            self.minHeapify(x)
            
    def __str__(self):
        result = ''
        for x in self.__list:
            result = result + str(x) + ','
        return '{' + result[:-1] + '}'
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:23:44 2021

@author: p4u13
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
p1 = Coordinate(5,7)
p2 = Coordinate(-3,17)

print(p1)
print(p2)

print(p1.distance(p2))
print(p2.distance(p1))

print(Coordinate.distance(p1, p2))
print(Coordinate.distance(p2, p1))

print(isinstance(p1, Coordinate))


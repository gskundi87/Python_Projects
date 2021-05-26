# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:18:20 2021

@author: p4u1
"""

from  createGraph import *

Q = []

while len(distances) != 0:
    u = distance.extractMin()
    vertices[2] = True
    for e in edges[u[1]]:
        if distance.
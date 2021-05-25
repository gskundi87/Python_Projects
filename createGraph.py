# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:19:59 2021

@author: p4u13
"""

from collections import defaultdict

vertex = defaultdict(list)

edge = defaultdict(list)

vertex['a'] = [('b', 2), ('c', 4)]

vertex['b'] = ['a', 'c', 'd', 'e']

vertex['c'] = ['a', 'b', 'd']

vertex['d'] = ['b', 'c', 'e', 'f', 'g']

vertedx['e'] = ['b', 'c']

vertex['f'] = ['b', 'c']

vertex['g'] = ['b', 'c']

vertex['h'] = ['b', 'c']


    
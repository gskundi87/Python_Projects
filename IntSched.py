# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:00:19 2021

@author: p4u1
"""

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    
    for j in range(p, r):
        if A[j][1] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
        
intervals = [(9, 12, 1), (5 ,7, 4), (3, 10, 7), (2, 6, 4), (1, 4, 2), (8, 11, 2)]

quicksort(intervals, 0, len(intervals) - 1)

record = [-1] * len(intervals)

def binarySearch(p, s, e, i, v):
    global record
    x = (s + e) // 2
    if p[x][1] < v:
        if record[i] == -1 or p[x][1] > p[record[i]][1]:
            record[i] = x
        if s >= e:
            return
        binarySearch(p, x + 1, e, i, v)
    else:
        if s >= e:
            return
        binarySearch(p, s, x - 1, i, v)

for i in range(0, len(intervals)):
    binarySearch(intervals, 0, len(intervals) - 1, i, intervals[i][0])

print(intervals)
print(record)

# RECURSIVE

def opt_rec(intervals, record, i):
    if i < 0:
        return 0

    value_if_not_taken = opt_rec(intervals, record, i - 1)

    value_if_taken = intervals[i][2] + opt_rec(intervals, record, record[i])

    return max(value_if_taken, value_if_not_taken)

credits = opt_rec(intervals, record, len(intervals) - 1)
print(credits)

# MEMOIZATION

def opt_mem(intervals, record, i, memo):
    if i < 0:
        return 0

    if memo[i] is -1:
        memo[i] = max(intervals[i][2] + opt_mem(intervals, record, record[i], memo),
                        opt_mem(intervals, record, i - 1, memo))
    
    return memo[i]

def get_intervals(intervals, record, memo):
    i = len(intervals) - 1
    result = []

    while i >= 1:
        if memo[i] > memo[i - 1]:
            result.append(intervals[i])
            i = record[i]
        else:
            i -= 1

    if i is 0:
        result.append(intervals[i])

    return result

memo = [-1] * len(intervals)
credits = opt_mem(intervals, record, len(intervals) - 1, memo)
result = get_intervals(intervals, record, memo)
print(memo)
print(credits)
print(result)

# ITERATIVE

def opt_iter(intervals, record, memo_dict):
    for i in range(len(intervals)):
        memo_dict[i] = max(memo_dict[i - 1], memo_dict[record[i]] + intervals[i][2])

    return memo_dict[len(intervals) - 1]

memo_dict = {-1: 0}
credits = opt_iter(intervals, record, memo_dict)
result = get_intervals(intervals, record, memo_dict)
print(memo_dict)
print(credits)
print(result)
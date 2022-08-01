import random
import math
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(x):
    for i in range(0,len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j][0] > x[j+1][0]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

def find_median(B):
    if len(B) <= 5:
        B = bubble_sort(B)
        return B[(len(B)-1)//2]
    g = len(B)//5
    temp = []
    end = 0
    for x in range(0,g):
        C = B[5*x:5*(x+1)]
        end = 5*(x+1)
        temp.append(find_median(C))
    if end < len(B):
        temp.append(find_median(B[end:len(B)]))
    return find_median(temp)

def find_max(A):
    maximum = A[0]
    for i in range(1,len(A)):
        if A[i][1] > maximum[1]:
            maximum = A[i]
    return maximum

def make_set(count, maximum1, maximum2):
    A = []
    
    for i in range(0,count):
        a = random.randint(0, maximum1)
        b = random.randint(0, maximum2)
        c = (a,b)
        A.append(c)
        
    return A

def minima_set_BF(A):
    B = A.copy()
    for i in range(0,len(A)):
        for j in range(0,len(A)):           
            if A[i][0] > A[j][0] and A[i][1] < A[j][1]:
                B.remove(A[i])
                break
    return B

def minima_set_DC(A):
    if len(A) <= 5:
        return minima_set_BF(A)
    p = find_median(A)
    L = [x for x in A if x[0] <= p[0]]
    G = [x for x in A if x[0] > p[0]]
    M1 = minima_set_DC(L)
    M2 = minima_set_DC(G)
    m = find_max(M1)
    temp = []
    for m2 in M2:
        if m2[1] > m[1]:
            temp.append(m2)
    return list(M1 + temp)  

# A = [(4,65),(8,15),(8.5,2),(2,35),(10,0),(9,85),(8.2,90)]

A = make_set(13,100,100)


D = A.copy()
E = A.copy()

points = np.array(A)

x,y = points.T

plt.scatter(x,y)
plt.show()

B = minima_set_DC(D)
C = minima_set_BF(E)

print(B)
print(C)
        
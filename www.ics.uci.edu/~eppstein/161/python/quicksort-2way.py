# quicksort, implemented similarly to the one in CLRS
# unfortunately will take quadratic time when all list entries are the same
# David Eppstein, UCI, 17 Jan 2002

import random
R = random.Random(42)

def qsort(L):
	quicksort(L,0,len(L))

def quicksort(L,start,stop):
	if stop - start < 2: return
	i = R.randrange(start,stop)
	swap(L,i,stop-1)
	split = partition(L,start,stop)
	quicksort(L,start,split)
	quicksort(L,split+1,stop)

def partition(L,start,stop):
	i = start
	j = stop-2
	key = L[stop-1]
	while i <= j:
		if L[i] <= key: i = i + 1
		elif L[j] >= key: j = j - 1
		else:
			swap(L,i,j)
			i = i + 1
			j = j - 1
	swap(L,i,stop-1)
	print [L,start,stop,i,key]
	return i
	
def swap(A,i,j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

L = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
qsort(L)
print L

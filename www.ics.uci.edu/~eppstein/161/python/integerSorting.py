# integer sorting routines: countingSort and radixSort
# David Eppstein, UC Irvine, 22 Jan 2002
#
# Both take as input a list of items, a function for turning items into
# integer keys, and a bound on the size of the key.
# We assume that, for each x in L, 0 <= key(x) <= maxkey;
# if not, bad things may happen (most likely, an exception will be raised).
#
# The radixSort routine also takes an input argument specifying which
# base to use.  I use bases 2 and 10 for clarity in the examples but
# a base closer to n would be better for practical efficiency;
# one could also require the base to be a power of two and replace the
# division and mod operations in radixSort by bitwise Boolean operations.
#
# The lambda expression in radixSort requires Python version 2.2 or greater;
# see http://python.sourceforge.net/peps/pep-0227.html for an explanation.

def countingSort(L,key,maxkey):
	N = [0]*(maxkey+1)
	for x in L:
		N[key(x)] = N[key(x)] + 1
        P = [0]*(maxkey+1)
	for i in range(maxkey):
		P[i+1] = P[i] + N[i]
	D = [None]*len(L)
	for x in L:
		D[P[key(x)]] = x
		P[key(x)] = P[key(x)] + 1
	return D

def radixSort(L,key,base,maxkey):
	divisor = 1
	while maxkey/divisor > 0:
		L = countingSort(L, (lambda x: (key(x)/divisor) % base), base-1)
		divisor = divisor * base
	return L


# some test cases
print countingSort([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9],(lambda x: x), 9)
print radixSort([31,14,41,15,59,92,26,53,35,58,89,97,79],(lambda x: x), 10,100)
print radixSort([31,14,41,15,59,92,26,53,35,58,89,97,79],(lambda x: x), 2, 100)

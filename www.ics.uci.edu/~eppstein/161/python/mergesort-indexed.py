# Mergesort, using indexing into arrays to run in O(n log n) time
# David Eppstein, UCI, 16 Jan 2002

def mergesort(L):
	if len(L) < 2: return L
	return merge(mergesort(L[:len(L)/2]),mergesort(L[len(L)/2:]))

def merge(A,B):
	Out = []
	iA = iB = 0
	while len(A)+len(B) > iA + iB:
		if len(B) <= iB or (len(A) > iA and A[iA] < B[iB]):
			Out.append(A[iA])
			iA = iA + 1
		else:
			Out.append(B[iB])
			iB = iB + 1
	return Out

print mergesort([3,4,1,5,9,2,6,5,3,5])

# quick sort, compact but inefficient list-copying implementation
# David Eppstein, UCI, 17 Jan 2002

import random
R = random.Random(42)

def qsort(L):
	if len(L) < 2: return L
	i = R.randrange(len(L))
	return qsort([x for x in L if x < L[i]]) + \
	       [x for x in L if x == L[i]] + \
	       qsort([x for x in L if x > L[i]])

print qsort([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9])

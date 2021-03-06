# optimal ordering for matrix chain products
# David Eppstein, ICS, UCI, 5 Feb 2002
#
# Due to use of nested scopes, this requires Python 2.2 or greater

# Input is a list L of dimensions.  The dimensions of matrix i
# are L[i]*L[i+1], so L represents a chain of len(L)-1 matrices.

# initial recursive algorithm
def MM1(L):
	if len(L) < 3: return 0
	return min([MM1(L[:k+1]) + MM1(L[k:]) + L[0]*L[k]*L[len(L)-1] \
			for k in range(1,len(L)-1)])

# Refactor to have numeric arguments
# Arguments i and j correspond to list L[i:j+1], i.e. starting at i
# and ending at j (inclusive).  This is not the typical Python
# convention but works better for this problem.
def MM2(L):
	def recur(i,j):
		if j-i < 2: return 0
		return min([recur(i,k) + recur(k,j) + L[i]*L[k]*L[j] \
				for k in range(i+1,j)])

	return recur(0,len(L)-1)
	
# Memoize: cache recursion values
def MM3(L):
	# two-dimensional array M[i][j]
	M = [None] * len(L)
	for i in range(len(L)): M[i] = [None] * len(L)

	def recur(i,j):
		if M[i][j] == None:
			if j-i < 2: M[i][j] = 0
			else: M[i][j] = min([recur(i,k) +\
				recur(k,j) + L[i]*L[k]*L[j] \
				for k in range(i+1,j)])
		return M[i][j]

	return recur(0,len(L)-1)

# Iterative computation of same recursion values
def MM4(L):
	# two-dimensional array M[i][j]
	M = [None] * len(L)
	for i in range(len(L)): M[i] = [0] * len(L)

	# loop over pairs (i,j) ordered by difference d=j-i
	for d in range(1,len(L)):
		for i in range(len(L)-d):
			j = i + d
			if j-i < 2: M[i][j] = 0
			else: M[i][j] = min([M[i][k]+M[k][j]+L[i]*L[k]*L[j] \
				for k in range(i+1,j)])

	# debugging output
	for i in range(len(L)): print M[i]

	return M[0][len(L)-1]

# Backtrack to output actual matrix product
def MM5(L):
	# two-dimensional array M[i][j]
	M = [None] * len(L)
	for i in range(len(L)): M[i] = [0] * len(L)

	# loop over pairs (i,j) ordered by difference d=j-i
	for d in range(1,len(L)):
		for i in range(len(L)-d):
			j = i + d
			if j-i < 2: M[i][j] = 0
			else: M[i][j] = min([M[i][k]+M[k][j]+L[i]*L[k]*L[j] \
				for k in range(i+1,j)])

	def recur(i,j):
		if j-i < 2:
			print L[i],"x",L[j],
		else:
			for k in range(i+1,j):
				if M[i][j] == M[i][k]+M[k][j]+L[i]*L[k]*L[j]:
					print "(",
					recur(i,k)
					print ") (",
					recur(k,j)
					print ")",
					return
		
	recur(0,len(L)-1)
	print

print MM1([3,10,2,20,6])
print MM2([3,10,2,20,6])
print MM3([3,10,2,20,6])
print MM4([3,10,2,20,6])
MM5([3,10,2,20,6])

# results:
#
# number of operations = 336
#
# L = [0, 0, 60, 180, 336]
#     [0, 0, 0, 400, 360]
#     [0, 0, 0, 0, 240]
#     [0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0]
#
# optimal ordering:
# ( ( 3 x 10 ) ( 10 x 2 ) ) ( ( 2 x 20 ) ( 20 x 6 ) )

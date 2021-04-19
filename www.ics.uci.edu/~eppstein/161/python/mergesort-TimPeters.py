# Tim Peters' optimized merge sort
# http://groups.google.com/groups?selm=mailman.1011233066.18504.python-list@python.org

def mergesort(A):
    "Sort list, via stable mergesort."
    n = len(A)
    B = [None] * n
    swapped = 0
    s = 1
    while s < n:
        s2 = s+s
        # Invariant:  viewing A as a sequence of slices of length s (plus
        # perhaps an oddball at the end), each slice is sorted.  (This is
        # trivially so when s=1; proceed by induction.)  Now merge adjacent
        # pairs of slices into sorted slices twice as large.
        for i in range(0, n, s2):
            ihi = j = i+s       # start of adjacent slice
            jhi = min(j+s, n)   # final slice may have an oddball size
            k = i               # start of output slice
            while i < ihi and j < jhi:
                if A[i] <= A[j]:
                    B[k] = A[i]
                    i += 1
                else:
                    B[k] = A[j]
                    j += 1
                k += 1
            # Copy tail.  At most one of these isn't vaccuous.
            B[k : k+ihi-i] = A[i : ihi]
            B[k : k+jhi-j] = A[j : jhi]
        # Swap input and output lists.
        A, B = B, A
        swapped = not swapped
        s = s2

    if swapped:  # copy back into original input list
        B[:] = A

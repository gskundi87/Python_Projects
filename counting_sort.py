import numpy

def counting_sort(A,k):
    L = [[] for _ in range(k)]
    n = len(A)

    for i in range(n):
        index = A[i]
        L[index].append(A[i])

    output = []

    for j in range(k):
        output.extend(L[j])

    return output

A = numpy.random.randint(0,100,10)

x = counting_sort(A,100)

print(x)

"""
Find the maximum product of two integers in an array
Given an integer array, find the maximum product of two integers in it.

For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.

"""

import sys
 
 
# A naive solution to finding the maximum product of two integers in a list
def findMaximumProduct(A):
 
    # base case
    if len(A) < 2:
        return
 
    max_product = -sys.maxsize
    max_i = max_j = -1
 
    # consider every pair of elements
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            # update the maximum product if required
            if max_product < A[i] * A[j]:
                max_product = A[i] * A[j]
                (max_i, max_j) = (i, j)
 
    print("Pair is", (A[max_i], A[max_j]))
 
 
if __name__ == '__main__':
 
    A = [-20, -3, 30, 6, -2]
    findMaximumProduct(A)
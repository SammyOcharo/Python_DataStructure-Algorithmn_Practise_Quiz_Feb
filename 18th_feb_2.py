"""
Sort an array of 0’s, 1’s, and 2’s (Dutch National Flag Problem)
Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.

For example,

Input:  { 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 }
 
Output: { 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2 }

"""

# Utility function to swap elements `A[i]` and `A[j]` in the list
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Linear time partition routine to sort a list containing 0, 1, and 2.
# It is similar to 3–way partitioning for the Dutch national flag problem.
def threeWayPartition(A):
 
    start = mid = 0
    pivot = 1
    end = len(A) - 1
 
    while mid <= end:
        if A[mid] < pivot:      # current element is 0
            swap(A, start, mid)
            start = start + 1
            mid = mid + 1
        elif A[mid] > pivot:    # current element is 2
            swap(A, mid, end)
            end = end - 1
        else:                   # current element is 1
            mid = mid + 1
 
 
if __name__ == '__main__':
 
    A = [0, 1, 2, 2, 2, 1, 2, 2, 0, 1, 1, 0]
    threeWayPartition(A)
    print(A)
 
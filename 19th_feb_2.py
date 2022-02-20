
from random import randrange
 
 
"""
Shuffle an array using Fisher–Yates shuffle algorithm
Given an integer array, in-place shuffle it. The algorithm should produce an unbiased permutation, 
i.e., every permutation is equally likely.

"""

# Utility function to swap elements `A[i]` and `A[j]` in a list
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Function to shuffle a list `A`
def shuffle(A):
 
    # read list from the highest index to lowest
    for i in reversed(range(1, len(A))):
 
        # generate a random number `j` such that 0 <= j <= i
        j = randrange(i + 1)
 
        # swap the current element with the randomly generated index
        swap(A, i, j)
 
 
if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5, 6]
 
    shuffle(A)
 
    # print the shuffled list
    print(A)
 
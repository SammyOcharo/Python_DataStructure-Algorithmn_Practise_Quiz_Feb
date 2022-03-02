"""
Shuffle an array using Fisher–Yates shuffle algorithm
Given an integer array, in-place shuffle it. 
The algorithm should produce an unbiased permutation, i.e., every permutation is equally likely.

"""

from random import randrange
#swaping function
def Swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def Shuffle(A):
    #read values from th list starting lowest to highest

    for i in range(len(A)-1):

        #lets generate a random number j to run from i to the n(the last number in the list)
        j = randrange(i, len(A))

        #lets call the swap funcion
        Swap(A, i, j)



if __name__ == '__main__':

    A = [1,2,3,4,5]

    Shuffle(A)

    print (A)

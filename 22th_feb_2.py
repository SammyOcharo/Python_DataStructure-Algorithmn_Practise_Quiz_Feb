"""
Rearrange an array with alternate high and low elements
Given an integer array, rearrange it such that every second element becomes greater than its left and right elements. 
Assume no duplicate elements are present in the array.

For example,

Input:  {1, 2, 3, 4, 5, 6, 7}
Output: {1, 3, 2, 5, 4, 7, 6}

"""
#function to swap the array elements
def Swap(A, i, j):

    temp = A[i]
    A[i]= A[j]
    A[j] = temp

def Rearrangefunction(A):

    for i in range (1, len(A), 2):
#if the previous element of the array is bigger we call the shuffle function
        if  A[i-1] > A[i]:
            Swap(A, i-1, i)
        
        if  A[i+1]> A[i]:
            Swap(A, i+1, i)


if __name__ == '__main__':

    A = [9, 6, 8, 3, 7]
 
    Rearrangefunction(A)

    print(A)
"""
Sort binary array in linear time
Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

For example,

Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
Output: { 0, 0, 0, 0, 1, 1, 1, 1 }

"""

# Function to sort a binary list in linear time



def sort(A):
 
    # count number of 0's
    zeros = A.count(0)
    k=0
    # put 0's at the beginning
    while zeros:
        A[k]=0
        zeros = zeros-1
        k=k+1
 
    # fill all remaining elements by 1
    for k in range(k, len(A)):
        A[k]=1
 
 
if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
 
    sort(A)
 
    # print the rearranged list
    print('sorted list is', A)
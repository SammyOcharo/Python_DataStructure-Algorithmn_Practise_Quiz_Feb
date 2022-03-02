"""
Move all zeros present in an array to the end
Given an integer array, move all zeros present in it to the end. 
The solution should maintain the relative order of items in the array and should not use constant space.

"""
def Swap(A, i, j):
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def ReallignZero(A):
    j = 0

    for i in range(len(A)):
        if A[i]:            # pivot is 0
            
            Swap(A, i, j)
            j = j + 1
        
    

if __name__ == '__main__':

    A = [4,0,2,2,4,0,0,0,0]

    ReallignZero(A)
    print(A)
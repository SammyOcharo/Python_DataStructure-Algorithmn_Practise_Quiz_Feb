"""
Find equilibrium index of an array
Given an integer array, find the equilibrium index in it.

"""




def Equilibrium(A):
    total = sum(A)

    right =0
    indeces = []

    for i in range(len(A)):

        if right == total -(A[i]+ right):
            indeces.append(i)

        right += A[i]
            
    print("Indeces that achieve equilibrium are", indeces)
if __name__ == '__main__':

    A =  [0, -3, 5, -4, -2, 3, 1, 0]

    Equilibrium(A)

    
    
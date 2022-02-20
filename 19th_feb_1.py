"""
In-place merge two sorted arrays
Given two sorted arrays, X[] and Y[] of size m and n each, merge elements of X[] with elements of array Y[] by maintaining the sorted order, i.e., fill X[] with the first m smallest elements and fill Y[] with remaining elements.

Do the conversion in-place and without using any other data structure.

 
For example,

Input:
 
X[] = { 1, 4, 7, 8, 10 }
Y[] = { 2, 3, 9 }
 
Output:
 
X[] = { 1, 2, 3, 4, 7 }
Y[] = { 8, 9, 10 }

"""


def mergeList(X, Y):
    
    n = len(X)
    m = len(Y)

    for i in range(n):

        if X[i] > Y[0]:
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp

            first = Y[0]

            k=1


            while k < m and Y[k] < first:
                Y[k-1] = Y[k]

                k = k+1
            
            Y[k-1] = first

        


if __name__ == '__main__':
    
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]

    mergeList(X, Y)

    print("X:", X)
    print("Y:", Y)
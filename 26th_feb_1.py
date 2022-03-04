"""
Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

def divisible_by_5(A):

    for i in range(len(A)):
        if A[i]%5 == 0:
            print(A[i], "is divisible by 5") 
        
        



if __name__ == '__main__':

    A = [10, 20, 33, 46, 55]

    divisible_by_5(A)
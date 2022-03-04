"""
Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
"""

def sum():
    
    for i in range(10):
        if i==0:
            j=0
            i = int(i)
            j = int(j)
            addition = i+j

            print("Current Number", i)
            print("Previous Number", j)
            print("Sum: ", addition)
            j = j+1
        
        else:
            j=i-1
            i = int(i)
            j = int(j)
            addition = i+j

            print("Current Number", i)
            print("Previous Number", j)
            print("Sum: ", addition)
            j = j+1

if __name__ == '__main__':

    print(sum())
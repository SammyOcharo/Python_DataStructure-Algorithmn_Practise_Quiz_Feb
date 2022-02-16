"""
    Find a pair with the given sum in an array
Given an unsorted integer array, find a pair with the given sum in it.
For example,

Input:
 
nums = [8, 7, 2, 5, 3, 1]
target = 10
 
Output:
 
Pair found (8, 2)
or
Pair found (7, 3)

"""


# Naive method to find a pair in a list with the given sum
def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums)-1):
        
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                print("The pair is", (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)
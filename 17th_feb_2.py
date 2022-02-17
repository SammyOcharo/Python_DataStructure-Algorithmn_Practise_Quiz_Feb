"""
Find the duplicate element in a limited range array
Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, 
find the duplicate number in it without using any extra space.

Input:  { 1, 2, 3, 4, 2 }
Output: The duplicate element is 2

"""

# Function to find a duplicate element in a limited range list
def findDuplicate(nums):
 
    # create a visited list of size `n+1`
    # we can also use a dictionary instead of a visited list
    visited = [False] * (len(nums) + 1)
 
    # for each element in the list, mark it as visited and
    # return it if seen before
    for i in nums:
 
        # if the element is seen before
        if visited[i]:
            return i
 
        # mark element as visited
        visited[i] = True
 
    # no duplicate found
    return -1
 
if __name__ == '__main__':
 
    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(nums)`
    nums = [1, 2, 3, 4, 4]
   
    print('The duplicate element is', findDuplicate(nums))


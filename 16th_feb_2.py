"""
Check if a subarray with 0 sum exists or not
Given an integer array, check if it contains a subarray having zero-sum.

"""
# Function to check if a sublist with zero-sum is present in a given list or not
def hasZeroSumSublist(nums):
 
    # create an empty set to store the sum of elements of each
   s=set()

    
 
    # insert 0 into the set to handle the case when sublist with
    # zero-sum starts from index 0
   s.add(0)

   total = 0
    # traverse the given list
   for i in nums:
 
        # sum of elements so far
        total += i
 
        # if the sum is seen before, we have found a sublist with zero-sum
        if total in s:
        # insert sum so far into the set
            return True
 
    # we reach here when no sublist with zero-sum exists
   return False
 
 
if __name__ == '__main__':
 
    nums = [4, -6, 2, -1, 4, 2, 7]
 
    if hasZeroSumSublist(nums):
        print('Sublist that adds to zero exists')
    else:
        print('Sublist that adds to zero does not exist')
 
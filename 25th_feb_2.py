"""
Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same.
 If numbers are different then return False.
"""
def checker(numbers_x, numbers_y):

    if numbers_x[-1]==numbers_y[-1]:
        print(True)
    else:
        print(False)


if __name__ == '__main__':

    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 20]

    checker(numbers_x, numbers_y)
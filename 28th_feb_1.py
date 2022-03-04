"""
Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

"""

def reverse(number):

    number1 = number[::-1]

    print(number1, " is the reversed number of ", number)


if __name__ == '__main__':

    number = input("Input number to be reversed: ")

    reverse(number)
"""
Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

"""

from numpy import number


def Palindrome(number):

    number1 = number[::-1]

    if number1 ==number:

        print(number1, " is a palindrome of number ")
    else:
        print (number, " is not a palindrome number")



if __name__ == '__main__':

    number = input("Input number to check if its a palindrome number: ")

    Palindrome(number)
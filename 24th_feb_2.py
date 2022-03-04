"""
Print characters from a string that are present at an even index number
For example, str = "pynative" so you should display p, n, t, v.
"""

def string(word):

    for i in word:
        print (i)




if __name__ == '__main__':

    word = input("Enter word: ")

    string(word)
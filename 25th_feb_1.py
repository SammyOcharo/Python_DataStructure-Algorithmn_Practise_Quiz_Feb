"""
 Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
"""

def remove_chars(word, How_many_characters_to_be_removed):
    if How_many_characters_to_be_removed > len(word):
        print("the characters you entered exceeds the number of characters of the provided word")
    else:
        print('Original string:', word)
        x = word[How_many_characters_to_be_removed:]
        print (x)



if __name__ == '__main__':

    word = input("Enter word: ")
    How_many_characters_to_be_removed = input("How_many_characters_to_be_removed: ")
    How_many_characters_to_be_removed = int(How_many_characters_to_be_removed)

    remove_chars(word, How_many_characters_to_be_removed)
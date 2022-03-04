"""
Create a new list from a two list using the following condition
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the 
new list should contain odd numbers from the first list and even numbers from the second list.

"""

def EvenOdd(list1, list2):

    list3 = []

    for i in range(len(list1)):
        if list1[i]%2 != 0:
            list3.append(list1[i])

    for j in range(len(list2)):
        if list2[j]%2 == 0:
            list3.append(list2[j])
    
    print(list3)



if __name__ == '__main__':


    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]

    EvenOdd(list1, list2)
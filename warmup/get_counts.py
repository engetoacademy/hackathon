#!/usr/bin/env python3
'''
Create a program that will print out how many times does every object occur inside
any list, tuple or string (counts of individual characters).
The program output should be a dictionary with counts associated with each value.


Input: [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
Output value: {'1': 4, '8': 1, '321': 1, '4': 1, '3': 2, '6': 2, '21': 1, '32': 1, '5': 2, '2': 3, '9': 1}

Bonus 1 (not tested):
Make a program to recognize, whether the input is list, tuple or a string. If it is
a string, then return the counts for each word.

Bonus 2 (not tested):
Print the result also as a table with nicely aligned numbers ordered from the
most frequent occurence to the least frequent occurence.

Example:

The above example printed to the screen - see the useful string methods section.
Printed to the screen:

 Item |Count
=============
 1    |  4
 2    |  3
 3    |  2
 5    |  2
 6    |  2
 32   |  1
 4    |  1
 321  |  1
 8    |  1
 9    |  1
 21   |  1


'''
seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

def main(seq):
    # check if the input sequence is empty - if so then the result should be
    # empty string


    # create a dictionary that will collect counts of each item in the sequence
    counts = {}

    # bonus 1 - if you want to count entire words, now it is time to split the
    # string to words



    # iterate over the sequence and increase the count of the item found




    # you can now return the result or you can continue trying to print
    # the results nicely

    # Bonus 2: find out, what column widths will need each column of the
    # table - use the len(), max(), and str() (if the item is a number)
    # functions to find the length of the longest item in the column -
    # beware, maybe the column headers will be the longest items in the column
    # column to the left will be made of dictionary keys (items), the right occurence
    # will be associated values






    # Bonus 2: Now it is time to print each row on new line

    # First print the header - center the 'Item' and 'Count' words inside the
    # string (str.center() method)


    # Now print each row with item and associated value - use the center() method
    # and the width of each column

    return counts


if __name__=='__main__':
    main(seq)

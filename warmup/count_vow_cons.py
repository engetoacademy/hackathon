#!/usr/bin/env python3
'''
Write a Python program that will count how many vowels and consonants are in
a given string.

The program should take as input a string and output a dictionary in form:
{'consonants':count_c, 'vowels':count_v}
count_c should be count of consonants
count_v - count of vowels

Example:
input sentence: 'a speech sound that is produced by comparatively open configuration of the vocal tract'
output: {'consonants':43, 'vowels':30}

'''
#input:
sentence ='''
Pandas is excellent at manipulating large amounts of data and summarizing
it in multiple text and visual representations. Without much effort, pandas
supports output to CSV, Excel, HTML, json and more.
'''


# function takes only one input - the sentence is a string
def main(sentence):
    # create two variables - one that will store a sequence of vowels and
    # the other to store the sequence of all the consonants

    # prepare the variable that will store dictionary where the counts of
    # vowels and consonants will be stored
    counts = {'vowels':0, 'consonants':0}

    # loop over the sentence and determine, whether a letter belongs to
    # the group of vowels or consonants



    return counts


if __name__=='__main__':

    main(sentence)

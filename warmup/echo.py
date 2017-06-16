#!/usr/bin/env python3
'''
Write a Python program that will create "echo sentences". Each word in
the sentence we will feed in, should be repeated n number of times. The number
of repetitions and the sentence to be manipulated are inputs into our function


If supplied the sentence:

    'I do not want to work today'

The output should be:

    'I I I do do do not not not want want want to to to work work work today today today'

You can also use the print() function to see the resulting string.

The resulting sentence cannot begin with space, unless the input sentence contained it

'''
# input:
sentence = 'I do not want to work today'
num_repeat = 3

def main(sentence,num_repeat):
    # get words using split method

    # create variable in this you will store the resulting string

    # iterate over the list of words you got in the previous step and repeat
    # each word num_repeat times

    # return result and strip spaces at its beginning and end



if __name__ == '__main__':
    main(sentence,num_repeat)

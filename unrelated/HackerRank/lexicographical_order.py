#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def swap(w, i, len_swappable):
    if len(w)-1 == i:
        return w
    if len(w) == 1:
        return w
    if len(w) == 2:
        return w[:i] + w[i+1] + w[i]
     return w[:i] + w[i+1:i+len_swappable] +  w[i] + w[i+len_swappable:]

def biggerIsGreater(w):
    temp = ''
    greater_word = w
    length_swappable = len(w)-1
    for i in range(length_swappable, 0, -1):
        for j in range(0, len(w), length_swappable):
            temp = swap(w, j, i+1)
        
            if temp > w:
                greater_word = temp
    if greater_word == w:
        return 'no answer'
    else:
        return greater_word


if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print()
        print(result + '\n')

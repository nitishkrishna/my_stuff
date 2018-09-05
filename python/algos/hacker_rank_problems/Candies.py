#!/bin/python

import math
import os
import random
import re
import sys

# Complete the candies function below.
# Idea: increase candies going left to right till you go past the local maxima, then backtrack adding one till you start going up in values again
def candies(n, arr):
    chocolates = []
    for i in range(n):
        chocolates.append(0)
    for i in range(n):
        if i == 0:
            chocolates[i] = 1
        if arr[i] > arr[i-1]:
            chocolates[i] = chocolates[i-1] + 1
        elif arr[i] == arr[i-1]:
            chocolates[i] = 1
        else:
            chocolates[i] = 1
            j = i
            while chocolates[j-1] <= chocolates[j] and j >= 0 and arr[j-1] > arr[j]:
                chocolates[j-1] += 1
                j = j - 1
    return sum(chocolates)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


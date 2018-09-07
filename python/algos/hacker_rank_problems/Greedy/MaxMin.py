#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    sorted_a = sorted(arr)
    min_sa = sys.maxsize
    cur = 0
    for i in range(0, len(sorted_a)-k+1):
        cur = sorted_a[i+k-1] - sorted_a[i]
        if cur<min_sa:
            min_sa = cur
    return min_sa
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    k = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

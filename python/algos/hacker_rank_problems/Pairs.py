#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    sorted_array = sorted(arr)
    i=0
    j=1
    count=0
    
    while(j < len(arr)):
        diff = sorted_array[j] - sorted_array[i]
        if (diff == k):
            count+=1
            j+=1
        elif (diff > k):
            i+=1
        elif (diff < k):
            j+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


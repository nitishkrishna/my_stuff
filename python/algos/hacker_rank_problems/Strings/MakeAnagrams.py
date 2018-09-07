#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    freq = [0]*26
    count = 0
    for c in a:
        freq[ord(c)-ord('a')]+=1
    for c in b:
        freq[ord(c)-ord('a')]-=1
    for f in freq:
        count += abs(f)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

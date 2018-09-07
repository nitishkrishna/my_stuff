#!/bin/python

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
# Idea: Buy the k costliest flowers at 1*price first
# Buy the next k costliest floweres at 2*price
# ... Buy the last k flowers at m*price

def getMinimumCost(n, k, c):
    cost = 0
    c = sorted(c, reverse=True)
    for i in range(0, n):
        cost += (i // k + 1) * c[i]
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    minimumCost = getMinimumCost(n, k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
step_dict = {}
step_dict[0] = 1
step_dict[1] = 1
def steps(n):
    c=0
    if n<0:
        return 0        
    if n in step_dict:
        return step_dict[n]
    else:
        c = steps(n-1) + steps(n-2) + steps(n-3)
        step_dict[n] = c
    return c

def stepPerms(n):
    c = steps(n)
    return c % 10000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

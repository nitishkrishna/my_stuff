#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for b in s:
        if b in ['(', '{', '[']:
            stack.append(b)
        elif b in [')', '}', ']']:
            if not len(stack):
                return "NO"
            top = stack[-1]
            if (top == '(' and b == ')') or \
                (top == '{' and b == '}') or \
                (top == '[' and b == ']'):
                stack.pop()
            else:
                return "NO"
        else:
            return "NO"
        
    if not len(stack):
        return "YES"
    else:
        return "NO"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

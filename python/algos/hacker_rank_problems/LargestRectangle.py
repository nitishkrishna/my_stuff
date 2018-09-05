#!/bin/python

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(n, h):
    stack = list()
    stack.append(0)
    max_area=0
    i=1
    while(i<n):
        if h[i] >= h[i-1]:
            stack.append(i)
        else:
            while(len(stack) and h[stack[-1]]<h[i]):
                new_h = h[stack.pop()]
                area = new_h*(i-stack[-1])
                if max_area < area:
                    area = max_area
            stack.append(i)
        i+=1
    while (len(stack)):
        new_h = h[stack.pop()]
        if len(stack):
            area = new_h*(i-stack[-1])
        else:
            area = new_h
        if max_area < area:
            area = max_area
            
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largestRectangle(n, h)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    d = {}
    for idx,val in enumerate(cost):
        if val not in d:
            d[val] = (money-val, idx)
        else:
            if money == 2*val:
                print str(d[val][1]+1) + " " + str(idx+1)
                return
    for k in d:
        if d[k][0] in d:
            idx1 = d[k][1]
            idx2 = d[d[k][0]][1]
            if idx1<idx2:
                print str(idx1+1) + " " + str(idx2+1)
            else:
                print str(idx2+1) + " " + str(idx1+1)
            return

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)

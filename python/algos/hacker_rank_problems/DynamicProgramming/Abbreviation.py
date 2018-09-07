#!/bin/python

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def delete_all_lower(a):
    new_word = ""
    for idx, char in enumerate(a):
        if char.islower():
            continue
        else:
            new_word+=char
    return new_word
            
def convert_to_upper(a,idx):
    new_a = a
    new_a = new_a[:idx] + new_a[idx].upper() + new_a[idx+1:]
    return new_a

def abb_helper(a,b,n_l,lc_list):
    #print a + " " + str(n_l) + " " + str(lc_list)
    
    result_list = []
    
    if len(a) < len(b):
        return False
    if a == b:
        return True
    if n_l == 0:
        return False
    
    if len(a) == len(b):
        for idx, val in enumerate(a):
            if (val != b[idx] or val.upper() != b[idx]):
                return False
        return True
    
    for idx, val in enumerate(lc_list):
        new_a = convert_to_upper(a,val)
        new_list = lc_list[:idx] + lc_list[idx+1:]
        #print new_a
        result_list.append(abb_helper(new_a,b,n_l-1,new_list))
    
    new_a = delete_all_lower(a)
    #print new_a
    result_list.append(abb_helper(new_a,b,0,[]))
    
    return any(result_list)

def abbreviation(a, b):
    n_l = 0
    lc_list = []
    for idx, char in enumerate(a):
        if char.islower():
            n_l +=1
            lc_list.append(idx)
    
    a_copy = a
    if abb_helper(a_copy,b,n_l,lc_list):
        return "YES"
    else:
        return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()


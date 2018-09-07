#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    d = {}
    for ws in range(0, len(s)):
        wl = 0
        d[ws] = {}
        while(wl+ws)<len(s):
            word = s[wl:wl+ws+1]
            char_set_word = "".join(sorted(word))
            print word
            if char_set_word not in d[ws]:
                d[ws][char_set_word] = 0
            else:
                print "match"
                d[ws][char_set_word] +=1
                count+=d[ws][char_set_word]
            wl+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

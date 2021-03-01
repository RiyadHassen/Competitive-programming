# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:21:18 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    pair =0
    #arr.sort()
    s = set(arr)
    for i in range(len(arr)):
        temp=arr[i]-k
        if temp in s:
            pair+=1
    return pair
                          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

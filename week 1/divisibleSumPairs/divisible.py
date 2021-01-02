# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:41:13 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    result = []
    j = 0
    for i in range(n):
        fix = ar[i]
        for j in range(i+1,n):
            if (fix + ar[j])% k == 0:
                result.append([i,j])
    return len(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:29:49 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    res = 0
    for s in n:
        res+=int(s)
    res *= k
    while res >= 10:
        res = sum_digit(res)
    return res
def sum_digit(n):
    res = 0
    val = int(n)
    while val > 10:
        res = res + val%10
        val = val // 10
    res += val
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

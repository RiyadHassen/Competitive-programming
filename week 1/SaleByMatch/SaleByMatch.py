# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:39:52 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sale={}
    pair=0
    for i in range(n):
        if str(ar[i]) in sale:
            sale[str(ar[i])]= sale[str(ar[i])] + 1
        else:
            sale[str(ar[i])] = 1
    for j in sale:
        if sale[j] //2 > 0:
            pair+=sale[j]//2
    print(sale)
    return pair
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

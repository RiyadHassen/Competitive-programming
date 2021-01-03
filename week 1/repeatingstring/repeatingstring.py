# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 00:21:24 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s = s.lower()
    no_a = s.count('a') 
    count = 0
    print(no_a)
    repeat = n // len(s)
    print(repeat)
    count = no_a * repeat
    rem = n % len(s)
    for i in range(rem):
        if s[i] == 'a':
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

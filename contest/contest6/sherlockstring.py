# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:35:38 2021

@author: riyad
"""

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    freq = Counter(s)
    setfreq =Counter(freq.values())
    if len(setfreq)==1:
        return 'YES'
    elif len(setfreq) == 2:
        first, second = setfreq.keys()
        if setfreq[first]==1 and  (first-1 ==0 or first-1==second):
            return 'YES'
        if setfreq[second]==1 and (second-1 ==0 or second-1==first):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

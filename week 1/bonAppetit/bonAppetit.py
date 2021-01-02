# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:20:15 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    faircost = 0 
    avg = 0
    noteatn = bill[k]
    for i in range(len(bill)):
        avg += bill[i]
    faircost = avg - noteatn
    faircost  = faircost //2
    
    if b == faircost:
        print('Bon Appetit')
    else:
        print(b -faircost)
    
    
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:53:46 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    count = 0 
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i-1 < 0:
                count+= A[i][j]
            else:
                temp = A[i][j] - A[i-1][j]
                if temp > 0:
                    count+=temp
    for i in range(len(A)-1,-1,-1):
        for j in range(len(A[i])):
            if i+1 == len(A):
                ##print(i,A[i])
                #print(j,A[i][j])
                count+= A[i][j]
            else:
                temp = A[i][j] - A[i+1][j]
                if temp > 0:
                    count+=temp
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j-1 < 0:
                count+= A[i][j]
            else:
                temp = A[i][j] - A[i][j-1]
                if temp > 0:
                    count+=temp
    for i in range(len(A)-1,-1,-1):
        for j in range(len(A[i])):
            if j+1 >= len(A[i]):
                count+= A[i][j]
            else:
                temp = A[i][j] - A[i][j+1]
                if temp > 0:
                    count+=temp
    count+= 2 * (len(A)*len(A[0])) 
        
    return count
                
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()


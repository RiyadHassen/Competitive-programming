# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:24:01 2021

@author: riyad
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys


def quickSort(ar):
    left,eq,right = partition(ar)
    if len(left) > 1:
        left = quickSort(left)
    if len(right)>1:
        right= quickSort(right)
    ar = left + eq + right
    #print(*ar)
    fptr.write(' '.join(map(str, ar)))  
    fptr.write('\n')
    return ar
# Complete the quickSort function below.
def partition(arr):
    if len(arr) < 1:
        return [],[],[]
    left,right = [],[]
    #i = 1
    for j in range(1,len(arr)):
        if arr[j] < arr[0]:
            #arr[j],arr[i]=arr[i],arr[j]
            left.append(arr[j])
            #i+=1
        elif arr[j]>arr[0]:
            right.append(arr[j])
    return left,[arr[0]],right
    
    #arr[0],arr[i-1] = arr[i-1],arr[0]
    #print(arr)
    #return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr = quickSort(arr)

    #fptr.write(' '.join(map(str, arr)))
    fptr.write('\n')

    fptr.close()

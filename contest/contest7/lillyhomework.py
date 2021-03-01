# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:16:15 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import copy
# Complete the lilysHomework function below.
def lilysHomework(arr):
    #variable declartion
    switch1 ,switch2 = 0 , 0
    arrpos, arrpos2 ,forward ,reverse = {},{},{},{}
    
    
    #array opreation
    arr2 = arr.copy()
    arrforward = sorted(arr)
    arrrev = arrforward[::-1]
   
    for i in range(len(arr)):
        arrpos[arr[i]]=i    
    for i in range(len(arrforward)):
        forward[arrforward[i]]=i
    for i in range(len(arrrev)):
        reverse[arrrev[i]] = i
    for ele in arrpos:
        if arrpos[ele] == forward[ele]:
            continue
        else:
            index1 = forward[ele]
            index2 = arrpos[ele]
            temp = arr[index1]
            arr[index1],arr[index2] = arr[index2],arr[index1]
            arrpos[ele] = index1
            arrpos[temp] = index2
            switch1+=1
    
    for i in range(len(arr2)):
        arrpos2[arr2[i]]=i
    for ele in arrpos2:
        if arrpos2[ele] == reverse[ele]:
            continue
        else:
            index1 = reverse[ele]
            index2 = arrpos2[ele]
            temp = arr2[index1]
            arr2[index1],arr2[index2] = arr2[index2],arr2[index1]
            arrpos2[ele] = index1
            arrpos2[temp] = index2
            switch2+=1
    return min(switch1,switch2)
        
        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

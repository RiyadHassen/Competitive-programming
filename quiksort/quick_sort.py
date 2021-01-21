# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:26:16 2021

@author: riyad
"""
import random

def quick_sort(ar):
    if len(ar)<=1:
        return ar
    
    print(ar)
    value = random.randrange(1,len(ar))
    first = partition(ar)[:value]
    second = partition(ar)[value+1:]
    quick_sort(first)
    quick_sort(second)
    return ar
    
        
        
        


# Complete the quickSort function below.
def partition(arr):
    p = arr[0]
    i = 1
    for j in range(1,len(arr)):
        if arr[j] < p:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[0],arr[i-1] = arr[i-1],arr[0]
    return arr

print(quick_sort([9,8,1,3,7,8,2]))
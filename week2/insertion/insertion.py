# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:42:05 2021

@author: riyad
"""

def insertionSort(nums):    
    for i in range(1,len(nums)):
        current = nums[i]
        while i >0 and current < nums[i-1]:
            nums[i]=nums[i-1]
            i -=1
        nums[i]=current
    return nums

print(insertionSort([5,4,3,2,1]))
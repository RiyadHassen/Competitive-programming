# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:27:46 2021

@author: riyad
"""

def getPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                count+=1
    return count
            


print(getPairs([1,2,3]))
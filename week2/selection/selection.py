# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:32:32 2021

@author: riyad
"""

def Selection(nums):
    for i in range(len(nums)):
        smallIdx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[smallIdx]:
                smallIdx = j
        if smallIdx !=i:
            nums[i],nums[smallIdx] = nums[smallIdx],nums[i]
    return nums        
print(Selection([5,4,3,2,1]))        
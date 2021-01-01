# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:21:38 2021

@author: riyad
"""

def twoSum(nums, target):
        result = []
        for i in range(len(nums)):
            temp  = target - nums[i]
            tempindex =nums[i+1:]
            if temp in tempindex:
                result.append(i)
                result.append(nums.index(temp,i+1))
                break
        return result
    
    
print(twoSum([2,11,15,7],9))    
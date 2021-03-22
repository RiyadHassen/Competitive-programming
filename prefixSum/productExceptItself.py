# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:19:13 2021

@author: riyad
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]
        l = len(nums)-1
        for i in range(len(nums)-1):
            result.append(result[-1]*nums[l-i])
        result = result[::-1]
        count =1
        for i in range(len(result)):
            result[i] = result[i] * count
            count = count*nums[i]
        return result
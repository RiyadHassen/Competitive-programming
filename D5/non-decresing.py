# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:29:08 2021

@author: riyad
"""

class Solution:
    def checkPossibility(self, nums):
        p = None
        for i in range(len(nums)- 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
    
    
            
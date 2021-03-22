# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:21:07 2021

@author: riyad
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d,count,result = {},0,0
        d[result]=1
        
        for i in range(len(nums)):
            result += nums[i]
            temp = result - k
            # k = result - temp
            if temp in d:
                count+= d[temp]
                
            if result not  in d:
                d[result] = 1
            else:
                d[result]+=1
            
        return count
        
        
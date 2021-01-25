# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:53:25 2021

@author: riyad
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        m= int(len(nums)/2)
        L1 = self.sortArray(nums[:m])
        L2 = self.sortArray(nums[m:])
        return merge(L1,L2)

    
    
    def merge(self,L1,L2):
        if not L1:return L2
        if not L2:return L1
        if L1[0] < L2[0]:
            return [L1[0]]+merge(L1[1:],L2)
        return [L2[0]]+merge(L1,L2[1:])
    

        
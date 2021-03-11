# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:20:39 2021

@author: riyad
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums,0,len(nums)-1,target)
        
    def binarysearch(self,nums,r,l,target):
        if r <= l:
            m =(l+r)//2
            if nums[m] == target:
                return m
            if nums[m]>target:
                return self.binarysearch(nums,r,m-1,target)
            else:
                return self.binarysearch(nums,m+1,l,target)   
        return -1
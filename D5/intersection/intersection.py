# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:13:40 2021

@author: riyad
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums1)):
            current = nums1[i]
            for j in range(len(nums2)):
                if current == nums2[j] and current not in result:
                    result.append(current)
        return result
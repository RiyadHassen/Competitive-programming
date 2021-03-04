# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:10 2021

@author: riyad
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h,result = [],[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                temp = nums1[i] + nums2[j]
                heapq.heappush(h,(temp,[nums1[i],nums2[j]]))
        
        for i in range(k):
            if len(h)!=0:
                res,pair = heapq.heappop(h)
                result.append(pair)
            if len(h)==0:
                break
        return result
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:15:21 2021

@author: riyad
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]] += 1            
        h =[]
        for item in d:
            heapq.heappush(h,(-1 * d[item],item))
        for i in range(k):
            result.append(heapq.heappop(h)[1])
            heapq.heapify(h)
        return result
        
            
            
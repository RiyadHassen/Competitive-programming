# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:14:05 2021

@author: riyad
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(stones)
        
        for stone in stones:
            heapq.heappush(h,-stone)
        print(h)
        while len(h) > 1:
            temp = abs(heapq.heappop(h)) - abs(heapq.heappop(h))
            if temp > 0:
                heapq.heappush(h,(-temp))
            heapq.heapify(h)
        if len(h)<1:
            return 0
        return abs(h[0])

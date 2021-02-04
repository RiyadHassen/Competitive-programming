# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:53:25 2021

@author: riyad
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        result = []
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        h = []
        for item in d:
            heapq.heappush(h,(-1 * d[item],item))
        for i in range(k):
            result.append(heapq.heappop(h)[1])
        return result
        
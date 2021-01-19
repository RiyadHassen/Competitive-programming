# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:00:50 2021

@author: riyad
"""

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(len(A)-1,-1,-1):
            if i >= 2:
                if(A[i]>=A[i-1] + A[i-2]):
                    continue
                else:
                    res = A[i]+A[i-1]+A[i-2]
                    return res
        return 0
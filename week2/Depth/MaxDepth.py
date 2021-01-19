# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:53:20 2021

@author: riyad
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        start = 0
        parent = 0
        end = 0
        count = 0
        for l in s:
            if l =='(':
                start += 1
                if parent > 0:
                    parent -= 1
            elif l ==')':
                parent += 1
                end+=1
            if parent > count:
                count =parent
            if start == end:
                parent = 0
                start = 0
                end =0 
        return count
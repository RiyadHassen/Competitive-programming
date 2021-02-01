# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:20:23 2021

@author: riyad
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = 0
        for i in range(len(logs)):
            if logs[i]=="../" and current > 0:
                current -=1
            elif logs[i][0] != '.':
                current+=1
        return current
    
            
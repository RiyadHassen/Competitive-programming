# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:20:17 2021

@author: riyad
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            negative = False
            start = 0
            end = len(grid[i])-1
            while start <= end:
                middle = start + ((end-start)//2)
                if grid[i][middle] < 0:
                    end = middle - 1
                    negative = True
                else:
                    start = middle+1
            if negative:
                count += (len(grid[i]))-start
        return count
            
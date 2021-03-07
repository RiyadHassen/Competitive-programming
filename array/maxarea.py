# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:08:18 2021

@author: riyad
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum,left ,right = 0,0,len(height)-1
        while left <= right:
            area = (right-left) * min(height[right],height[left])
            maximum = max(maximum,area)
            if height[left]<height[right]:
                left+=1
            else:
                right -=1
        return maximum
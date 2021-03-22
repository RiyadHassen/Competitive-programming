# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:18:20 2021

@author: riyad
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, visited,maximum = 0,0,set(),0
        while(right < len(s)):
            if s[right] in visited:
                visited.remove(s[left])
                left +=1 
                
            else:
                visited.add(s[right])
                maximum = max(maximum,(right-left)+1)
                right+=1
        return maximum   
                
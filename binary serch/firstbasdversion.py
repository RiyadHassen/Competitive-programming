# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:03:57 2021

@author: riyad
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n 
        l = 0
        b = 0
        while(l <= r):
            m = l  +  (r- l)//2;
            if isBadVersion(m):
                b = m
                r = m -1
            else:
                l = m + 1
                
        return b
   
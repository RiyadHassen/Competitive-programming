# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:58:59 2021

@author: riyad
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        iterr = 2
        t1 = 0
        t2= 1
        t3 = 1
        tri = 0
        if n ==0:
            return t1
        elif n>0 and n<3:
            return t2  
        while iterr <  n:
            tri = t1 + t2 + t3
            t1 = t2
            t2 = t3
            t3 = tri
            iterr+=1
        return tri
    
            
            
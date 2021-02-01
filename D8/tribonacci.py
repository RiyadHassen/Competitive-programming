# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:59:43 2021

@author: riyad
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 2 :
            return 1
        else:
            return  self.tribonacci(n-1)+self.tribonacci(n-2) + self.tribonacci(n-3)
        
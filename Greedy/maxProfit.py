# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:16:13 2021

@author: riyad
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i] - prices[i-1])
        return max_profit
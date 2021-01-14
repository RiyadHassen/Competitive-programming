# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:01:46 2021

@author: riyad
"""

def maximumToys(prices, k):
    prices.sort()
    temp = 0
    count = 0 
    for item in prices:
        temp+=item
        if temp <= k:
            count+=1
    return count


print(maximumToys([1,12,5,111,200,1000,10],50))


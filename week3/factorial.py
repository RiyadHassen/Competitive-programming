# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:50:35 2021

@author: riyad
"""

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(0))
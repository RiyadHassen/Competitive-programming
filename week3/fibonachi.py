# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:08:39 2021

@author: riyad
"""

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:39:55 2021

@author: riyad
"""

def fibiter(n):
     i=0
     fib = 0
     while i <= n:
         fib = fib + i
         i+=1
         
     return fib
print(fibiter(5))
    
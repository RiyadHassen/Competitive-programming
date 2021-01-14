# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:39:55 2021

@author: riyad
"""

def fibiter(n):
     i=1
     fib = 0
     a1 = 1
     a2 = 1
     while i <= n:
         fib =a1 + a2
         a1= a2
         a2 = fib
         i+=1
         
     return fib
print(fibiter(3))
    
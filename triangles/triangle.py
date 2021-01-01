# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 23:32:39 2020

@author: riyad
"""
def triangle1(n):
    for i in range(1,n+1):
        print(i *"*")
print(triangle1(5))
def triangle2(n):
    for i in range(1,10,2):
        print(((10-i)//2)*" "+""+i*"*"+((10-i)//2)*" ")
        
triangle2(5)
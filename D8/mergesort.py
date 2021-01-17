# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:23:39 2021

@author: riyad
"""

def merge(L1,L2):
    if not L1:return L2
    if not L2:return L1
    if L1[0] < L2[0]:
        return [L1[0]]+merge(L1[1:],L2)
    return [L2[0]]+merge(L1,L2[1:])

print(merge([2,100,300],[5,150]))

def mergesort(L):
    if len(L) <= 1:
        return L
    m= int(len(L)/2)
    L1 = mergesort(L[:m])
    L2 = mergesort(L[m:])
    return merge(L1,L2)

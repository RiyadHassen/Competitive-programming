# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:50:53 2021

@author: riyad
"""

def surfaceArea(A):
    count=0
    for i in range(len(A)):
        for j in range(len(i)):
            count+= A[i][j] * 6
            if i-1 < 0:
                pass
            if j-1 < 0: 
                pass
            #case for  A[i][j]
            if A[i+1][j] > A[i][j]:
                count-=A[i][j] 
            count -= A[i+1][j]
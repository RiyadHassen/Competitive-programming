# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:11:42 2021

@author: riyad
"""

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [[i, j] for i in range(R) for j in range(C)]
        keys=[]
        for  k in range(len(result)):
            temp= abs(r0 - result[k][0]) + abs(c0-result[k][1])
            keys.append(temp)
        
        sorted(result,key=keys)
               sorted([[i, j] for i in range(R) for j in range(C)], key=lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))
        return result
    
        
        
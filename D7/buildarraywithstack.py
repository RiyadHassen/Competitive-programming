# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:19:14 2021

@author: riyad
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        #nums = [i for i in range(1,n+1)]
        
        result = []
        #nums=[i for i in range(1,n+1)]
        tar= 0
        for i in range(1,target[-1]+1):
            if tar<=len(target)-1:
                if i ==target[tar]:
                    result.append("Push")
                    tar+=1
                else:
                    result.append("Push")
                    result.append("Pop")
        return result
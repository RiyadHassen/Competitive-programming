# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:09:31 2021

@author: riyad
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        common=[]
        distinct=[]
        for i in range(len(arr2)):
            current =arr2[i]
            for j in range(len(arr1)):
                if current ==arr1[j]:
                    common.append(arr1[j])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                distinct.append(arr1[i])
        distinct.sort()   
        return common+distinct
                    
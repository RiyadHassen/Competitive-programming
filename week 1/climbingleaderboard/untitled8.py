# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:42:05 2021

@author: riyad
"""

def insertionSort(nums):
    sort = []
    for i in range(len(nums)):
        if len(sort) ==0:
            sort.append(nums[i])
        else:
            for j in range(len(sort)):
                if sort[j] > nums[i]:
                    sort[j],nums[i]=nums[i],sort[j]
                    
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:08:10 2021

@author: riyad
"""

def bubleSort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] < nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
        print(nums)
    return nums
print(bubleSort([5,4,3,2,1]))



def buble(nums):
    for k in range(1,len(nums)):
        for i in range(len(nums)-k):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
        print(nums)
    return nums
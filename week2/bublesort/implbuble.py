# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:45:07 2021

@author: riyad
"""

def buble(nums):
    for k in range(1,len(nums)):
        for i in range(len(nums)-k):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
        print(nums)
    return nums

#print(buble([5,4,3,2,1]))

def bubleImproved(nums):
    needNextPass = True
    k = 1
    while k < len(nums) and needNextPass:
        needNextPass = False
        for i in range(len(nums)-k):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1]= nums[i+1],nums[i]
                needNextPass = True
        k+=1
        print(nums)
    return nums
            
print(bubleImproved([5,4,3,2,1]))
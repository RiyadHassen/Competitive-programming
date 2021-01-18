# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:02:50 2021

@author: riyad
"""

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1,0,-1):
            for j in range(1,i+1):
                if arr[j]==i+1:
                    result.append(j+1)
                    arr = self.flip(arr,j+1)
                    break
            arr = self.flip(arr,i+1)
            result.append(i+1)
        return result
    def flip(self,nums,index):
        return nums[:index][::-1] + nums[index:]
    

class Solution2:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr),0,-1):
            for j in range(1,i):
                if arr[j]==i:
                    result.append(j+1)
                    arr = self.flip(arr,j+1)
                    break
            arr = self.flip(arr,i)
            result.append(i)
        return result
    def flip(self,nums,index):
        return nums[:index][::-1] + nums[index:]
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:19:06 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        result = self.add_node(nums)
        return result
    def add_node(self,nums,result=None):
        if not nums:
            return result
        
        maximum = max(nums)
        left_nums = nums[0:nums.index(maximum)]
        right_nums=nums[nums.index(maximum)+1:]
        if not result:
            result = TreeNode(maximum)
            print(result)
            # return result
        
        result.left = self.add_node(left_nums, result.left)
        result.right = self.add_node(right_nums, result.right)
        return result
        
        
        
        
            
        
        
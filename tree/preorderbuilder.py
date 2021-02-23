# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:41:49 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        result = self.build(preorder)
        return result
    def build(self,preorder,result=None):
        if len(preorder)==0:
            return result
        rootnode = preorder[0]
        right_nums=[]
        left_nums=[]
        for i in range(1,len(preorder)):
            if preorder[i] < rootnode:
                left_nums.append(preorder[i])
            else:
                right_nums=preorder[i:]
                break
        if not result:
            result = TreeNode(rootnode)
        result.left = self.build(left_nums, result.left)
        result.right = self.build(right_nums, result.right) 
        return result
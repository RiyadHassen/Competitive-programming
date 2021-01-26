# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:00:05 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result1 =[]
        result2= []
        self.helper(p,result1)
        self.helper(q,result2)
        return result1 == result2
    
    def helper(self,root,result):
        if root==None:
            return result.append(None)
        result.append(root.val)
        self.helper(root.left,result)
        self.helper(root.right,result)
            
        
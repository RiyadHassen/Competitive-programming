# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:16:43 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        #print(root)
        return self.sumtarget(root,targetSum)
    def sumtarget(self,node,target):
        if not node.left and not node.right:
            return node.val
        if node.left:
            left = self.sumtarget(node.left,target) 
            print(left)
            #print(left)
            if left == target:
                return True
        if node.right:
            right = self.sumtarget(node.right,target) + node.val
            print(right)
            if right == target:
                return True
            
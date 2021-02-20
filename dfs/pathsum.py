# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:14:00 2021

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
    #     #print(root) 
    #     if not root:
    #         return False
    #     return self.sumtarget(root,targetSum,root.val)
    # def sumtarget(self,node,target,currentsum):
    #     if not node.left and not node.right:
    #         return currentsum==target
    #     left = False
    #     right = False
    #     if node.left:
    #         left = self.sumtarget(node.left,target,node.left.val+currentsum)
    #     if node.right:
    #         right = self.sumtarget(node.right,target,node.right.val+currentsum)
    #     return left or right
        if not root:
            return False
        return self.sumtarget(root,targetSum,0)
    def sumtarget(self,node,target,currentsum):
        if not node:
            return False
        currentsum+=node.val
        if not node.left and not node.right:
            return currentsum==target
        return self.sumtarget(node.left,target,currentsum) or self.sumtarget(node.right,target,currentsum)

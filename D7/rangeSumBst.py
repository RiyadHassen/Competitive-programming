# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:52:45 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = [0]
        self.helper(root,low,high,result)
        return result[0]
    def helper(self,root,low,high,res):
        if root == None:
            return 0
        if root.val >= low and root.val <= high:
            res[0] += root.val
        self.helper(root.left,low,high,res)
        self.helper(root.right,low,high,res)
        
#         result = 0 
#         if root.val >=low and root.val <=high:
#             result+=root.val
#         while root.left != None:
#             if root.val >=low and root.val <=high:
#                 result+=root.val 
            
#         while root.right!=None:
#             if root.val >=low and root.val <=high:
#                 result+=root.val 
        
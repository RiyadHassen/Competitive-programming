# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:53:58 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.helper(root)[0]
    def helper(self,root):
        if not root:
            return (0,0)
        if not root.left and not root.right:
            return (root.val,1)
        ##
        left = self.helper(root.left)
        ##print(left)
        right =self.helper(root.right)
        if left[1] < right[1]:
            return (right[0],right[1]+1)
        else:
            return  (left[0],left[1]+1)
        
        
        
                        
        
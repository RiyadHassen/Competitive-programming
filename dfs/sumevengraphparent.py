# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:16:22 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root)
    def helper(self,node,parent=1):
        if not node.right and not node.left:
            return 0
        total = 0
        if node.left:
            if parent%2==0:
                total+=node.left.val
            total+= self.helper(node.left,node.val)
        if node.right:
            if parent%2==0:
                total+=node.right.val
            total+= self.helper(node.right,node.val)
        return total
    
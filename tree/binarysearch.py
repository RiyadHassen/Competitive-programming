# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:56:17 2021

@author: riyad
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root!=None:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return None
        
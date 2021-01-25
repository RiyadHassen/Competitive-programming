# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:25:51 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.helper(root,val)
        return root
    def helper(self,root,val):
        if root.val > val and root.left == None:
            root.left = TreeNode(val)
        elif root.val < val and root.right==None:
            root.right = TreeNode(val)
        elif val < root.val:
            self.helper(root.left, val)
        else:
            self.helper(root.right, val)
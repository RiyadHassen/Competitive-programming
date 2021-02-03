# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:13:39 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        minum=-float('inf')
        maxnum = float('inf')
        return self.helper(root,minum,maxnum)
        
    def helper(self,root,minum,maxnum):
        if not root:
            return True
        if root.val <= minum or root.val >= maxnum:
                return False
        left = self.helper(root.left,minum,root.val)
        right = self.helper(root.right,root.val,maxnum)
        return left and right
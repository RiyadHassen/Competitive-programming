# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:13:34 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_uni = [0]
        self.univalue(root,max_uni)
        
        return max_uni[0]
    def univalue(self,root,max_uni):
        if not root.left and not root.right:
            return (0,root.val)
        leftval = (0,float('inf'))
        rightval = (0,float('inf'))
        if root.left:
            leftval = self.univalue(root.left,max_uni)
        if root.right:
            rightval = self.univalue(root.right,max_uni)
        print(leftval,rightval)
        if root.val == leftval[1] and root.val == rightval[1]:
            max_uni[0] = max(max_uni[0],leftval[0]+rightval[0]+2)
            return (max(rightval[0],leftval[0])+1,root.val)
        if root.val == leftval[1]:
            max_uni[0] = max(max_uni[0],leftval[0]+1)
            return (leftval[0]+1,root.val)    
        if root.val == rightval[1]:
            max_uni[0] = max(max_uni[0],rightval[0]+1)
            return (rightval[0]+1,root.val)
        return (0,root.val)
            
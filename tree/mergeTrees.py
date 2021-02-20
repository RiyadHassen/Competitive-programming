# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:15:57 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.helper(t1,t2)
    def helper(self,t1,t2):
        if not t1 and not t2:
            return 
        if t1 and t2:
            t1.val = t1.val + t2.val
        elif not t1 and  t2:
            t1 = t2
            return t1
        elif not t2:
            return t1
        if t2.left:
            t1.left =self.helper(t1.left,t2.left)
        if t2.right:
            t1.right = self.helper(t1.right,t2.right)
        return t1
        
        
        
        # if not t1 and not t2:
        #     return 
        # if  t1 and not t2:
        #     temp= TreeNode()
        #     temp.val = t1.val
        #     return temp
        # if t2 and not t1:
        #     temp = TreeNode()
        #     temp.val = t2.val
        #     return temp
        # if t1 and t2:
            
        
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:25:39 2021

@author: riyad
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        result = TreeNode()
        self.helper(root,result)
        
        return result
        
    def helper(self,root,result):
        if not root:
            return 
        result.val = root.val
        templ = copy.copy(root.left)
        tempr = copy.copy(root.right)
        result.right = templ 
        result.left = tempr
        #print("result=",result)
        #print("root=",result)
        self.helper(root.left,result.right)
        self.helper(root.right,result.left)
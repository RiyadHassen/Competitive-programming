# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:18:30 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root,result)
        return result
            
    def helper(self,root,result):
        if root != None:
            self.helper(root.left,result)
            self.helper(root.right,result)
            result.append(root.val)
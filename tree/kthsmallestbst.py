# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:05:03 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = [0]
        return self.kthSmallestBst(root,k,count)
    def kthSmallestBst(self,node,k,count):
        if not node:
            return 0
        left = self.kthSmallestBst(node.left,k,count)
        if left:
            return left
        count[0] = count[0]+1
        if count[0]==k:
            return node.val   
        return self.kthSmallestBst(node.right,k,count)
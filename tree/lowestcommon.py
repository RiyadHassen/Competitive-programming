# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:55:42 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left,p,q)
            if root.val <p.val and root.val <q.val:
                return self.lowestCommonAncestor(root.right,p,q)
            else:
                return root
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:48:03 2021

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
            return self.common(root,p,q)
        def common(self,root,p,q):
            if not root.left and not root.right :
                return root
            if root == p or root==q:
                return root
            left = None
            right =None
            if root.left:
                left = self.common(root.left,p,q)
            if root.right:
                right = self.common(root.right,p,q)
            if left == p and right ==q and root!=q and root!=p:
                return root
            if left == q and right ==p and root!=q and root!=p:
                return root
            if left ==p or right==q and root==q and root==p:
                # print(left, right)/
                if left:
                    return left
                return right
    
            # if root.left and not root.right:  
            #     if root==p and left==q:
            #         return root
            # right = self.common(root.right,p,q)
            # if root.right and not root.left:
            #     if root==p and right==q:
            #         return root
            # if root.right and root.left:
            #     if left ==p and right==q:
            #         return root
        
    
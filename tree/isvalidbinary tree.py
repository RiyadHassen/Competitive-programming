# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:29:48 2021

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
        result =[]
        self.helper(root,result)
        print(result)
        isValid = True
        for i in range(1,len(result)):
            if result[i-1] < result[i]:
                isValid =True
            else:
                isValid =False
                break
        return isValid
    def helper(self,root,result):
        if not root:
            return
        self.helper(root.left,result)
        result.append(root.val)
        self.helper(root.right,result)
        
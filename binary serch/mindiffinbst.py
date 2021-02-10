# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:15:08 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #result =[float('inf')]
        max_num = float('inf')
        min_num = -float('inf')
        return self.min_diff(root,min_num,max_num)
        #return result[0]
    def min_diff(self,root,min_num,max_num):
        if not root:
            return float('inf')
        mini = float('inf')
        if min_num!=-float('inf'):
            mini = min(root.val-min_num,mini)
        if max_num!=float('inf'):
            mini =min(max_num-root.val,mini)
        if not root.left and not root.right:
            return mini
        left =self.min_diff(root.left,min_num,root.val)
        right =self.min_diff(root.right,root.val,max_num)
        return min(left,right,mini)
        #print(min_num[0])
        # return min_num[0] 
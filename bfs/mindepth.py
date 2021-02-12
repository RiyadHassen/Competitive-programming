# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:16:21 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self,root):
        return root.left==None and root.right==None
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                if(self.is_leaf(front)):
                    return level
                if front.right:
                    queue.append(front.right)
                if front.left:
                    queue.append(front.left)
            level+=1
            
        return level
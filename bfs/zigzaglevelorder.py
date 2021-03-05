# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:22:24 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue,leftFirst,result = deque([]),False,[]
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if leftFirst:
                temp = temp[::-1]
                
            result.append(temp)
            if not leftFirst:
                leftFirst = True
            else:
                leftFirst = False
        return result
                
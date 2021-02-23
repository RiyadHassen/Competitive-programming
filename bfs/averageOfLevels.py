# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:32:26 2021

@author: riyad
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue,result = deque([]),[]
        queue.append(root)
        while queue:
            temp = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp/size)
        return result
                
            
        
        
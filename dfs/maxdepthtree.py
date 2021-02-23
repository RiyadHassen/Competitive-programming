# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:15:20 2021

@author: riyad
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return self.dfs(root)
        #DFS
    def dfs(self,node):
        depth = 0
        child = 0
        if not node.children:
            return 1
        for i in range(len(node.children)):
            child =self.dfs(node.children[i]) + 1
            depth=max(depth,child)
        #depth+= max(depth,child)
        return depth  
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit

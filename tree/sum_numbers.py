# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        chain = ""
        return self.dfs(root,total,chain)
        
    def dfs(self,node,total,chain):
        if not node.left and not node.right:
            chain += str(node.val)
            total+= int(chain)
            chain= chain[:-1]
            return total
        left = 0
        right = 0
        chain = chain + str(node.val)
        if node.left:
            left = self.dfs(node.left,total,chain)
        if node.right:
            right = self.dfs(node.right,total,chain)
        return left+right
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        node_collector,memo =[],{}
        max_product,sum_node = 0 ,0
        total = self.sum_tree(root,memo)
        self.preorder(root,node_collector)
        print(node_collector)
        for node in node_collector:
            sum_node = self.sum_tree(node,memo)
            prod = sum_node * (total - sum_node)
            max_product = max(prod,max_product)
        return (max_product % (10**9 + 7))
        
    def preorder(self,node,node_collector):
        if not node:
            return 
#         
#            sum_left = sum_tree(node.left)
#             max_product[0] = max(max_product[0],(total-sum_left)*sum_left)
#         if node.right:
#             sum_left = sum_tree(node.right)
#             max_product[0] = max(max_product[0],(total-sum_left)*sum_left)
            
        node_collector.append(node)
        self.preorder(node.left,node_collector)
        self.preorder(node.right,node_collector)
    
    
    def sum_tree(self,node,memo):
        if not node:
            return 0
        if node in memo:
            return memo[node]
        
        left= self.sum_tree(node.left,memo)
        right =self.sum_tree(node.right,memo)
        memo[node] = node.val + left +right
        return  memo[node]
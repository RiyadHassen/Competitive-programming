# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.constructBst(nums,0,len(nums)-1)
    def constructBst(self,nums,left,right):
        if (left > right):
            return 
        mid = left + (right - left) // 2
        current = TreeNode(nums[mid])
        current.left = self.constructBst(nums,left,mid-1)
        current.right = self.constructBst(nums,mid+1,right)
        return current
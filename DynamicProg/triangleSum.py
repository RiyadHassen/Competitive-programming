class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo ={}
        return self.min_path(triangle,0,0,memo)
    def min_path(self,triangle,row,col,memo):
        if row==len(triangle):
            return 0
        if (row,col) in memo:
            return memo[(row,col)]
        left = self.min_path(triangle,row+1,col,memo)
        right = self.min_path(triangle,row+1,col+1,memo)
        memo[(row,col)] = triangle[row][col]+min(left,right)
        return memo[(row,col)]
    
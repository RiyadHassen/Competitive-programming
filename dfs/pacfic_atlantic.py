class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_ocean = set()
        atlantic_ocean =set()
        
        #pacfic to atlantic
        
        for index in range(len(heights)): 
            self.dfs(heights,[0,index],pacific_ocean)
        left_to_right
        for index in range(len(heights)):
            self.dfs(heights,[index,0],pacific_ocean)
        #Atlantic to pacfic
        for index in range(len(heights)):
            self.dfs(heights,[index,-1],atlantic_ocean)
        for index in range(len(heights)):
            self.dfs(heights,[-1,index],atlantic_ocean)
        z = pacific_ocean.intersection(atlantic_ocean)
        return list(z)
    def dfs(self,matrix,index,sets):
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for direct in directions:
            move = (index[0]+direct[0],index[1]+direct[1])
            if 0 <= move[0] < len(matrix) and 0 <= move[1] < len(matrix[0]):
                if matrix[index[0]][index[1]] <= matrix[move[0]][move[1]]:
                    sets.add(move)
                    self.dfs(matrix,move,sets)
                    
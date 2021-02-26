# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:33:26 2021

@author: riyad
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum,visited = 0,set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    temp = self.dfs(grid,(i,j),visited)
                    if (i,j) not in visited:
                        temp =grid[i][j]
                    maximum= max(temp,maximum)
                    print(maximum)
        return maximum
    def dfs(self,grid,pos,visited):
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        temp = 0
        for direct in directions:
            move = (pos[0] + direct[0] , pos[1] + direct[1])
            if 0 <= move[0]< len(grid) and 0<= move[1] < len(grid[0]):
                if grid[move[0]][move[1]] == 1 and move not in visited:
                    visited.add(move)
                    temp+=self.dfs(grid,move,visited) + 1
                    #print(temp,move)
        return temp
            
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:44:52 2021

@author: riyad
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue,visited,minute = deque([]),set(),0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visited.add((i,j))
        print(queue)
        while queue:
            size = len(queue)
            isChanged =False
            for i in range(size):
                row,col = queue.popleft()
                for dre in direction:
                    move = (dre[0]+row,dre[1]+col)
                    if 0<= move[0]< len(grid) and 0<=move[1] < len(grid[0]):
                        if move not in visited:
                            if grid[move[0]][move[1]]==1:
                                grid[move[0]][move[1]]=2
                                isChanged =True
                                queue.append(move)
                                visited.add(move)
            if isChanged:
                minute+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return minute

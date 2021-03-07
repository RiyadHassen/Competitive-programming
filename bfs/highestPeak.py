# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:24:40 2021

@author: riyad
"""

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue,visited = deque([]), set()
        directions = [ [1,0], [-1,0], [0,1], [0,-1] ]
        
        #height = [[-1]*len(isWater[0])]*len(isWater)
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]== 1:
                    queue.append((i,j))
                    isWater[i][j]=0
                    visited.add((i,j))
        while queue:
            size = len(queue)
            for i in range(size):
                row,col = queue.popleft()
                for dre in directions:
                    move =  (dre[0]+row,dre[1]+col)
                    if 0 <= move[0]< len(isWater) and 0 <=move[1] < len(isWater[0]):
                        if move not in visited:
                            isWater[move[0]][move[1]]=isWater[row][col]+1
                            queue.append(move)
                            visited.add(move)            
        return isWater
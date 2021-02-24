# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:59:00 2021

@author: riyad
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited,provience = set(),0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and (i,j) not in visited:
                    self.dfs(i,(i,j),isConnected,visited)
                    provience+=1
        print(visited)            
        return provience
    def dfs(self,start,pos,isConnected,visited):
        visited.add(pos)
        for i in range(len(isConnected[start])):
            if isConnected[start][i]==1 and (start,i) not in visited:
                self.dfs(i,(start,i),isConnected,visited)
                
        
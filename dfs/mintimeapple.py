# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 07:36:39 2021

@author: riyad
"""

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        #adjcency list_rep
        d,visited,timetocollect={},set(),0
        for i in range(len(edges)):
            if edges[i][1] not in d:
                d[edges[i][1]] = edges[i][0]
            else:
                d[edges[i][0]]=edges[i][1]
        for ele in d:
            if hasApple[ele] and ele!=0:
                timetocollect += 2*(self.dfs(ele,visited,d))
        return timetocollect
    def dfs(self,ele,visited,graph):
        level = 0 
        if ele not in visited and ele!=0:
                visited.add(ele)
                level= self.dfs(graph[ele],visited,graph)+1
        return level
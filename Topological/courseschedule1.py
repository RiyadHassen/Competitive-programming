# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:14:54 2021

@author: riyad
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue,count = deque([]),0
        indgree,adj_list={},{}
        for pre in prerequisites:
            if pre[1] not in adj_list:
                adj_list[pre[1]]=[pre[0]]
            else:
                adj_list[pre[1]].append(pre[0])
        for i in range(numCourses):
            indgree[i]= 0 
        for pre in prerequisites:
            indgree[pre[0]]+= 1
        for dgree in indgree:
            if indgree[dgree]==0:
                queue.append(dgree)
        print(indgree,adj_list)
        while queue:
            ele = queue.popleft()
            count+=1
            if ele in adj_list:
                for child in adj_list[ele]:
                    indgree[child]-=1
                    if indgree[child]==0:
                        queue.append(child)
        return count==numCourses
                           
                
                
        
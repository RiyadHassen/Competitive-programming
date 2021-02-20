# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:17:13 2021

@author: riyad
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employ_dict ={}
        for i in range(len(employees)):
            if employees[i].id not in employ_dict:
                employ_dict[employees[i].id] = employees[i]
                
        return self.importance(employ_dict,id)
        
    def importance(self,employees,id):
        total_importance= 0
        #visited.add(employees[id].id)
        #for i in range(len(employees)):
            #if employees[0].id not in visited:
        for sub in employees[id].subordinates:
            total_importance+=self.importance(employees,sub) 
        total_importance+=employees[id].importance
        return total_importance
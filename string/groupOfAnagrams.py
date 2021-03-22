# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:23:16 2021

@author: riyad
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d ,result = {},[]
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in d:
                d[temp]=[s]
            else:
                d[temp].append(s)
        for key in d:
            result.append(d[key])
        return result
                
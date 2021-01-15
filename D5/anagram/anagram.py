# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:03:11 2021

@author: riyad
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
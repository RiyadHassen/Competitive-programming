# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:59:32 2021

@author: riyad
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = False
        if s==t:
            return True
        if len(s)> len(t) or len(s) < len(t):
            return False
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == s[j]:
                anagram = True
                
            else:
                anagram = False
                break
        return anagram
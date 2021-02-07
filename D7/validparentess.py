# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:04:42 2021

@author: riyad
"""

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for item in s:
            if item =='(':
                result.append('(')
            elif  item=="[":
                result.append('[')
            elif item =="{":
                result.append('{')
            elif item==")":
                if len(result)==0:
                    return False
                if result[-1]=='(':
                    result.pop(-1)
                elif result[-1]!='(':
                    return False
            elif item=="]":
                if len(result)==0:
                    return False
                if result[-1]=='[':
                    result.pop(-1)
                elif result[-1]!='[':
                    return False
            elif item=="}":
                if len(result)==0:
                    return False
                if result[-1]=='{':
                    result.pop(-1)
                elif result[-1]!='{':
                    return False  
        return len(result)==0
    
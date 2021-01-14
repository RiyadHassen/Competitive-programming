# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:20:39 2021

@author: riyad
"""

def vps(inputstr):
        if inputstr == "":
            return True
        elif inputstr[0] == '(' and  inputstr[-1] != ')':
            return False
        elif inputstr[0]=='(' and inputstr[-1]==')':
            return True
print(vps("(AB"))
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:45:09 2021

@author: riyad
"""

class Solution:
    def reverse(self, x):
        if x >= 0:
            intstr = str(x)
            zeroindex=0
            zeroindexed =False
            rev = intstr[::-1]
            for i in range(len(rev)):
                if len(rev) == 1:
                    break
                if rev[i] =='0' and rev[zeroindex]=='0':  
                    zeroindex = i
                    zeroindexed=True
                else:
                    break
            if zeroindexed:
                rev = rev[zeroindex+1:]
            if int(rev) > (2**31 - 1):
                return 0
            return rev
        elif x < 0 :
            x = abs(x)
            intstr = str(x)
            zeroindex=0
            zeroindexed =False
            rev = intstr[::-1]
            for i in range(len(rev)):
                if len(rev) == 1:
                    break
                if rev[i] =='0' and rev[zeroindex]=='0':  
                    zeroindex = i
                    zeroindexed=True
                else:
                    break
            if zeroindexed:
                rev = rev[zeroindex+1:]
            rev = '-'+rev
            if int(rev) < (-2**31):
                return 0
            return rev
        
        
        
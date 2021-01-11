# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:02:35 2021

@author: riyad
"""
val1 = eval(input("input first number:-"))
val2 = eval(input("input second number:-"))


def summation(val1,val2):
    val1 = str(val1)
    val2=str(val2)
    rem = 0
    result = ""
    #making the digits equal
    if len(val1) > len(val2):
        rev = val2[::-1]
        for i in range(len(val1)-len(val2)):
            rev = rev +'0'
        val2 = rev[::-1]
    else:
        rev = val1[::-1]
        for i in range(len(val2)-len(val1)):
            rev = rev +'0'
            val1 = rev[::-1]
            
    for i in range(len(val1)-1,-1,-1):
        temp = int(val1[i]) + int(val2[i]) + rem
        if temp > 9:
            rem = 1
            result = result + str(temp % 10)
        else:
            result = result + str(temp)
            rem = 0
    return result[::-1]

def sumnegative(val1,val2):
    #assuming val1 is postive and val2 is negative
    if val1 <0 and val2 < 0:
        val1= str(val1)[1:]
        val2 =str(val2)[1:]
        result = summation(val1,val2)
        return '-'+result
     if val1 < 0 and val2 > 0:
        temp = val1
        val1 = val2
        val2 = temp
    


print(sumnegative(val1,val2))
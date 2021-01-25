# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:29:25 2021

@author: riyad
"""

def countingsort(arr):
    countarr = [0 for i in range(max(arr)+1)]
    
    for i in range(len(arr)):
        countarr[arr[i]] +=1
    #print(countarr)
    
    for i in range(1,len(countarr)):
        countarr[i] = countarr[i]+countarr[i-1]
    #print(countarr)
    result =[0 for i in range(len(arr))]
    for i in range(len(arr)):
        #index of arr[i]
        index = countarr[arr[i]]
        result[index-1]= arr[i]
        countarr[arr[i]] -=1
    #print(result)
    return result


print(countingsort([5,4,2,1,3]))        
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:15:00 2021

@author: riyad
"""

# -*- coding: utf-8 -*-



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


def multiple(val1,val2):
    val1 = str(val1)
    val2=str(val2)
    rem = 0
    sumvalue = "" 
    total = '0'
    counter = 0 
    first = len(val1)
    second = len(val2)
   
    for i in range(second-1,-1,-1):
        for j in range(first-1,-1,-1):
            current = int(val2[i]) * int(val1[j]) + rem
            if current > 9:
                if j==0:
                    sumvalue+=str(current%10)
                    sumvalue+=str(current//10)
                else:
                    rem = current //10
                    sumvalue += str(current%10)
            else:
                rem = 0
                sumvalue += str(current)
        sumvalue=sumvalue[::-1]
        
        for k in range(counter):
            sumvalue+='0'
        #print(sumvalue)
        total = summation(total,sumvalue)
        sumvalue =""
        rem = 0
        counter+=1
    return total    
    #print(total)
                
if __name__=="__main__":
    val1 = input("input number 1 :-")
    val2 = input("input number 2  :-")
    #print(multiple(val1,val2))

 
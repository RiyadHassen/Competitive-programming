# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:39:41 2021

@author: riyad
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2): 
        rem = 0
        head  = None
        current1 = l1
        current2 = l2
        prev = None
        while current1 != None:
            result=ListNode()
            if(current2!=None):
                temp= current1.val + current2.val + rem
                if temp > 9:
                    rem  = temp //10
                    temp = temp % 10
                    result.val=temp
                    if head==None:
                        head= result
                        prev = head
                    else:
                        prev.next = result
                        prev  = result
                else:
                    result.val = temp
                    rem = 0 
                    if head==None:
                        head= result
                        prev = head
                    else:
                        prev.next = result
                        prev  = result
                current2 = current2.next
            else:
                temp = current1.val + rem
                if temp > 9:
                    rem  = temp //10
                    temp = temp % 10
                    result.val=temp
                    prev.next = result
                    prev = result
                else:
                    result.val = temp
                    prev.next = result
                    prev = result
                    rem = 0
            current1 = current1.next
        while current2!= None:
            result=ListNode()
            temp = current2.val + rem
            if temp > 9:
                rem  = temp //10
                temp = temp % 10
                result.val=temp
                prev.next = result
                prev = result
            else:
                result.val = temp
                prev.next = result
                prev = result
                rem = 0
            current2 = current2.next
        if rem > 0:
            result = ListNode()
            result.val = rem
            prev.next = result
        return head
                
        
        
        
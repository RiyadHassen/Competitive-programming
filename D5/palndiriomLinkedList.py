# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:15:29 2021

@author: riyad
"""

import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        reversed = self.reverse(copy.deepcopy(head))
        print(reversed)
        print(head)
        pal =False
        while head and reversed:
            if head!=reversed:
                pal =False
            else:
                pal = True
            head = head.next
            reversed = reversed.next
        if pal:
            return True
        return False
        
        
    def reverse(self,head,prev= None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self.reverse(n,head)
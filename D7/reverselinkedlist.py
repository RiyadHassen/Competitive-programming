# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:25:05 2021

@author: riyad
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:

        return self.helper(head, prev = None)
    def helper(self,head,prev= None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self.helper(n,head)
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:44:24 2021

@author: riyad
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        l2.next = self.mergeTwoLists(l1,l2.next)
        return l2
                
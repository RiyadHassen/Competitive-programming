# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:21:04 2021

@author: riyad
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        result = ListNode()
        while fast!= None and fast.next != None :
            slow = slow.next
            fast = fast.next.next # none.next
        return slow
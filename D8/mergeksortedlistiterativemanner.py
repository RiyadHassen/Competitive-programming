# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:09:32 2021

@author: riyad
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return None
        for i in range(1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i-1],lists[i])
        return lists[-1]
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        current =None
        while l1 and l2:
            if l1.val < l2.val:
                if not result:
                    result = ListNode(l1.val)
                    current=result
                    l1 = l1.next
                else:
                    temp = ListNode(l1.val)
                    current.next = temp
                    current = temp
                    l1=l1.next
            else:
                if not result:
                    result = ListNode(l2.val)
                    current=result
                    l2 = l2.next
                else:
                    temp = ListNode(l2.val)
                    current.next = temp
                    current = temp
                    l2=l2.next
        if l2 :
            if result:
                current.next = l2
            else:
                result = l2
        if l1:
            if result:
                current.next = l1
            else:
                result = l1
        return result
                
                
                
            
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:32:23 2021

@author: riyad
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #print(len(lists))
        #the idea is to get two elment from the list and sort them,
        #then append it back in the list
        if len(lists)==0:
            return None
            
        i =0 
        while len(lists) > 1:
            new= self.mergeTwoLists(lists[i],lists[i+1])
            lists = lists[i+2:]
            lists.append(new)
        return lists[0]
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        l2.next = self.mergeTwoLists(l1,l2.next)
        return l2
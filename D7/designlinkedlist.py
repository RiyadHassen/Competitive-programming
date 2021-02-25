# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:02:30 2021

@author: riyad
"""

from pprint import pprint
class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        count = 0
        current = self.head
        #found = False
        while current !=None:
            if count == index:
                #found = True
                return current.val
            else:
                current = current.next
                count+=1
        return -1
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be              the first node of the         linked list.
        """
        if self.head== None:
            self.head = Node(val)
            self.tail = Node(val)
        else:
            new = Node(val)
            new.next = self.head
            self.head = new 
        #if self.head.next:
            #print(self.head.next.next)
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail==None:
            self.head = Node(val)
            self.tail = Node(val)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            new = Node(val)
            current.next = new
            self.tail = current.next
    def print_node(self):
        current =self.head
        while current != None:
            print(str(current.val)+"->",end="")
            current= current.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked             list,the node will be  appended to the end of linked list. If index is greater than the length, the node will 
        not be inserted.
        """
        if index < 0 :
            return 
        if index==0:
            self.addAtHead(val)
            return
        count = 0
        current = self.head
        while current !=None and count < index-1:
            count+=1
            current = current.next
        if index > count + 1:
            return 
        new = Node(val)
        new.next = current.next
        if current.next==None:
            self.tail = new
        current.next = new
           
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return None
        prev = self.head
        current = self.head
        count=0
        while current.next !=None and count <= index:
            if count == index:
                if index ==0:
                    self.head = current.next
                prev.next = current.next
                current =None
                return
            else:
                prev = current
                current = current.next
                count +=1
        if index==count:
            prev.next=None
            current =None
            self.tail = prev
        if index > count:
            return
        self.print_node()
        return None
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
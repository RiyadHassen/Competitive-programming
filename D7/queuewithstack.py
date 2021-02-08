# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:49:17 2021

@author: riyad
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue =[]
        self.stack_back = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.stack_back = self.queue[::-1]
        
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self.stack_back.pop(-1)
        self.queue = self.stack_back[::-1]
        return res
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack_back[-1]
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_back)==0
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
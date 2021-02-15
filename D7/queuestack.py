# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:02:07 2021

@author: riyad
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        #self.queue2 =deque()        
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop()        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
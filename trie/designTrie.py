# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:09:06 2021

@author: riyad
"""

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # self.insertHelper(self.trie,word,0)
        # print(self.trie.children)
        current = self.trie
        for char in word:
            if char not in current.children:
                current.children[char]=Node()  
            current = current.children[char]
        current.isEnd = True
        
        
    # def insertHelper(self,trie,word,index):
    #     if index == len(word):
    #         return 
    #     if word[index] not in trie.children:
    #         trie.children[word[index]]=Node()
    #         if index == len(word)-1:
    #             trie.children[word[index]].isEnd = True
    #             return 
    #     else:
    #         if index == len(word)-1:
    #             trie.children[word[index]].isEnd = True
    #             return 
    #         else:
    #             self.insertHelper(trie.children[word[index]],word,index+1)
                
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.trie
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.isEnd 
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.trie
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True
        
class Node:
    def __init__(self):
        self.children ={}
        self.isEnd = False
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

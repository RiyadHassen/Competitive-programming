class Solution:
    def __init__(self):
        self.trie = Node()
        
    def build_dict(self,dictionary):
        for word in dictionary:
            self.insert(word)     
    def insert(self,word):
        current = self.trie
        for char in word:
            if char not in current.children:
                current.children[char]=Node()
            current = current.children[char]
        current.isEnd = True
    def search_root(self,word):
        res = ""
        current = self.trie
        for char in word:
            if char not in current.children or current.isEnd:
                break
            else:
                res+=char
            current = current.children[char]
        if current.isEnd:
            return res
        else: return ""
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = ""
        self.build_dict(dictionary)
        for word in sentence.split():
            if self.search_root(word) =="":
                result= result+' '+word
            else:
                result = result+' '+self.search_root(word)
        return result[1:]
    
class Node:
    def __init__(self):
        self.children ={}
        self.isEnd = False
        
        
        
        
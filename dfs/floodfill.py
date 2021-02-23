# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:39 2021

@author: riyad
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited =set()
        spos = (sr,sc)
        scolor = image[sr][sc]
        image[spos[0]][spos[1]]=newColor
        return self.fillImage(image,visited,spos,scolor,newColor)
    def fillImage(self,image,visited,spos,scolor,newColor):
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        for direct in directions:
            move = (direct[0]+spos[0],direct[1]+spos[1])
            #print(move)
            if 0 <= move[0] < len(image) and 0 <= move[1]<len(image[0]):
                print(move)
                #print(image)
                if image[move[0]][move[1]]== scolor:
                    if move not in visited:
                        visited.add(move)
                        image[move[0]][move[1]] = newColor
                        self.fillImage(image,visited,move,scolor,newColor)
        return image
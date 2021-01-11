# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:18:39 2021

@author: riyad
"""

def climbBoard(board,score):
    board.sort()
    board.reverse()
    leader = []
    count = 1
    current = board[0]
    leader.append(count)
    newboard=[]
    for i in range(1,len(board)):
        if board[i] == current:
            leader.append(count)
        else:
            count+=1
            leader.append(count)
        current = board[i]
    for i in range(len(score)):
        l = len(newboard)
        for j  in range(len(board)):
            if score[i] - board[j] < 0:
                continue
            elif score[i] - board[j] == 0:
                 newboard.append(leader[j])
                 break
            else:
                if leader[j] == 1:
                    newboard.append(1)
                    break
                else:
                    newboard.append(leader[j])
                    break
        if l == len(newboard):
            newboard.append(leader[-1]+1)
        
    return newboard


print(climbBoard([100,100,50,40,40,20,10],[5,25,50,120]))
            
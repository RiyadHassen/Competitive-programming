# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:34:31 2021

@author: riyad
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from collections import defaultdict

# Complete the bfs function below.
def bfs(n, m, edges, s):
    result,adj_list,visited,edge_weight = [-1] * n, defaultdict(set), set(),6
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    queue = deque([(1,s)])
    visited.add(s)
    while  queue:
        level,current = queue.popleft()
        for neb in adj_list[current]:
            if neb not in visited :
                visited.add(neb)
                #if result[neb-1] == -1:
                result[neb-1] = ((level)*edge_weight)
                queue.append((level+1,neb))
    result.pop(s-1)
    return result
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

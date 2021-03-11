class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue,visited = deque([]),set()
        maxdist = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    queue.append((0,i,j))
                    visited.add((i,j))
        if len(queue)==0 or len(queue)== len(grid)*len(grid[0]):
            return -1
        while queue:
            dist,row,col= queue.popleft()
            maxdist = max(dist,maxdist)
            for dre in directions:
                move = (row+dre[0],col+dre[1])
                if 0<=move[0]<len(grid) and 0<= move[1] < len(grid[0]):
                    if move not in visited:
                        queue.append((dist+1,move[0],move[1]))
                        visited.add(move)
        return maxdist
                
        
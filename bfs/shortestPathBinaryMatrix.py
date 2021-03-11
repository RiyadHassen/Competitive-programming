class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue,clear_path,visited= deque([]),0,set()
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
        end = (len(grid)-1,len(grid[0])-1)
        if grid[0][0]==1 or grid[end[0]][end[1]] ==1:
            return -1
        queue.append((1,0,0))
        visited.add((0,0))
        while queue:
            dist,row,col = queue.popleft()
            clear_path = max(clear_path,dist)
            if row==end[0] and col==end[1]:
                break
            for dre in directions:
                move = (row+dre[0],col+dre[1])
                if 0<= move[0] < len(grid) and 0<= move[1] <len(grid[0]):
                    if move not in visited and grid[move[0]][move[1]]==0:
                        queue.append((dist+1,move[0],move[1]))
                        visited.add(move)
        if end in visited:
            return clear_path
        return -1
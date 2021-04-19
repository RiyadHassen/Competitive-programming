class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        maximum=0
        memo = [0]*len(arr)
        for i in range(len(arr)):
            if memo[i]!=0:
                maximum= max(maximum,memo[i]) 
            else:
                maximum= max(maximum,self.dfs(i,arr,d,memo)) 
        return maximum  
    def dfs(self,index,arr,d,memo):
        if memo[index]!=0:
            return memo[index]
        moves = []
        for i in range(1,d+1):
            if 0<= index+i < len(arr):
                if arr[index] > arr[index+i]:
                    moves.append(index+i)
                else:
                    break
        for i in range(1,d+1):
            if 0<= index-i<len(arr):
                if arr[index] > arr[index-i]:
                    moves.append(index-i)
                else:
                    break
        level = 1
        max_level = 1
        for move in moves:
            level = self.dfs(move,arr,d,memo)+1
            max_level = max(level,max_level)
        memo[index]=max_level
        return memo[index]
    
            
            
            
            
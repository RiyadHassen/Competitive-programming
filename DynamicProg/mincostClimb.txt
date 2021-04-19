class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo ={}
        min_costfirst = self.climb(0,cost,memo)
        min_costsecond = self.climb(1,cost,memo)
        return min(min_costfirst,min_costsecond)
    def climb(self,stair,cost,memo):
        if stair > len(cost) -1:
            return 0
        if stair in memo:
            return memo[stair]
        climbcost = cost[stair] + min(self.climb(stair+1,cost,memo),self.climb(stair+2,cost,memo))
        memo[stair] = climbcost
        return memo[stair]
         
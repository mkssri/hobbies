class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n=len(cost)
        dp=[0]*(n+2)

        for i in range(n-1,-1,-1):
            jump1 = cost[i]+dp[i+1]
            jump2 = cost[i]+dp[i+2]
            dp[i] = min(jump1,jump2)
        
        return min(dp[0],dp[1])
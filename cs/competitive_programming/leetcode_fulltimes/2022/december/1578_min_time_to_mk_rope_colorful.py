class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        res = curr = 0

        l = len(neededTime)

        for i in range(l):

            if i>0 and colors[i] != colors[i-1]:
                curr = 0
            
            res = res + min(curr, neededTime[i])
            curr = max( curr,neededTime[i] )

        return res
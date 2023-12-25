class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # don't know following dp does not work lol!
        # dp = [[0]*cols]*rows

        # First row set to 1 except if there is an obstacle
        for c in range(cols):
            if(obstacleGrid[0][c]==1):break
            dp[0][c] = 1

        # First column set to 1 except if there is obstacle
        for r in range(rows):
            if(obstacleGrid[r][0]==1):
                break
            dp[r][0] = 1

        for r in range(1,rows):
            for c in range(1,cols):
                if(obstacleGrid[r][c]==1):
                    continue
                dp[r][c] = dp[r-1][c]+dp[r][c-1]

        return dp[-1][-1]
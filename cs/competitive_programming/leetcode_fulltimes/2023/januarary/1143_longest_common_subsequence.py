#Bottom UP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for r in range(len(text1)-1,-1,-1):
            for c in range(len(text2)-1,-1,-1):
                if text1[r]==text2[c]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]
    
#TOPDOWN
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        I=len(text1)
        J=len(text2)

        dp=[[0 for j in range(J+1)]for i in range(I+1)]

        for i in range(1,I+1):
            for j in range(1,J+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[I][J]
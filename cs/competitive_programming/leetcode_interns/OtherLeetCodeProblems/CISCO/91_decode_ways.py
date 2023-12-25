#!/usr/bin/python3

# Link - https://leetcode.com/problems/decode-ways/

# Youtube Solution - https://www.youtube.com/watch?v=6aEyTjOwlJU

"""
Two solutions possible
S1 - Depth For Search Using Recursion
S2 - Iterative using dynamic Programming
"""


# DFS using Recursion

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s) : 1}
        
        def dfs(i):
            
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            print("i is {}".format(i))
            
            # We took Signle digit
            res = dfs(i + 1)
            
            # 1<0-9> and 2<0-6>
            if(i + 1 < len(s) and ( s[i] == "1"\
                or (s[i] == "2" and s[i+1] in "0123456") )):
                res += dfs(i+2)
                
            dp[i] = res
            print("dp is {}".format(dp))
            return res
        
        return dfs(0)
    
# ITERATIVE SOLUTION 
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""
class Solution1(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = {len(s) : 1}
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                
            
            if(i+1 < len(s) and (s[i] == "1" \
                or s[i] == "2" and s[i+1] in "0123456")):
                    dp[i] += dp[i+2]
            print("dp is {}".format(dp))

                    
        return dp[0]
            

if __name__ == "__main__":
    
    obj = Solution1()
    s = "1212"

    out = obj.numDecodings(s)
    print(out)



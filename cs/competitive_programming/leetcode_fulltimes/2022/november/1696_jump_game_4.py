"""
Time Complexity: O(N^2)
TLE
"""

from typing import List
import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]

        for i in range(1,n):
            dp[i] = nums[i]+max(dp[max(0,i-k):i])
        
        return dp[-1]
    
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        h = [(-nums[0],0)]

        for i in range(1,n):

            while(h[0][1]<i-k):
                heapq.heappop(h)

            # We use heap just to get previous max_so_far
            # instead of dp! :)
            max_so_far = h[0][0]
            heapq.heappush(h,(max_so_far-nums[i],i))

            if i == n-1:
                return -1*(max_so_far-nums[i])
        
        return nums[0]
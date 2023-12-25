#!/usr/bin/python3

# Leetcode Link - https://leetcode.com/problems/maximum-subarray/

from typing import List
import math

# Timelimit exceeded

"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sub_array_sum = -math.inf
        
        for i in range(0, len(nums)):
            
            sub_array_sum = 0
            
            for j in range(i, len(nums)):
                
                sub_array_sum += nums[j]
                
                max_sub_array_sum = max(max_sub_array_sum, sub_array_sum)
        
        return max_sub_array_sum
        

# Dynamic Programming
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
Whenever you see a question that asks for the maximum or minimum of something, 
consider Dynamic Programming as a possibility. 
"""

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sub_array_sum, current_sub_array_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            
            current_sub_array_sum = max(nums[i], current_sub_array_sum+nums[i])
            max_sub_array_sum = max(max_sub_array_sum, current_sub_array_sum)
            
            
        return max_sub_array_sum


obj = Solution1()
nums = [-2,1,-3,4,-1,2,1,-5,4]
out = obj.maxSubArray(nums)

print(out)

nums = [5,4,-1,7,8]
out = obj.maxSubArray(nums)

print(out)
#!/usr/bin/python3

# Leetcode Link - https://leetcode.com/problems/product-of-array-except-self/

from typing import List

"""
Time Complexity - O(N)
Space Complexity - O(1)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        res = [1]*len(nums)
        
        prefix_val = 1
        
        for i in range(0, len(nums)):
            
            res[i] = prefix_val
            prefix_val *= nums[i]
        
        post_val = 1
        
        for j in range(len(nums)-1,-1,-1):
            
            res[j] *= post_val
            post_val *= nums[j]
        
        return res


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_lst = [1]*len(nums)
        post_lst = [1]*len(nums)
        
        res_lst = [1]*len(nums)
        
        prefix_val = 1
        
        for x in range(0, len(nums)):
            
            prefix_lst[x] = prefix_val
            prefix_val *= nums[x]
            
        post_val = 1
        
        for x in range(len(nums)-1, -1, -1):
            
            post_lst[x] = post_val
            post_val *= nums[x]
        
        
        for x in range(0,len(nums)):
            prefix_lst[x] = prefix_lst[x]*post_lst[x]
        
        
        return prefix_lst
            
                
            
            
        

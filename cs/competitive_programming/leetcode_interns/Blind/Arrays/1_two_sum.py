#!/usr/bin/python3

# Link - https://leetcode.com/problems/two-sum/

from typing import List



"""
Time Complexity - O(N)
Space Complexity - O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        
        for x in range(len(nums)):
            
            nums_dict[nums[x]] = x 
            
        # print(nums_dict)

        for x in range(len(nums)):
            
            complement = target - nums[x]
            
            
            if complement in nums_dict.keys() and x != nums_dict[complement]:
                return [x, nums_dict[complement]]
                
            
            
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        nums_dict = {}
        
        for i in range(len(nums)):
            
            nums_dict[nums[i]] = i
        
        
        for j in range(len(nums)):
            
            complement = target - nums[j]
            
            if complement in nums_dict.keys() and nums_dict[complement] != j:
                return [j, nums_dict[complement]]
            
            
        
        
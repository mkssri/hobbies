#!/usr/bin/python3

# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        nums.sort()
        
        
        for i in range(0, len(nums)):

            if nums[i] > 0:
                break
                
            if i == 0 or nums[i] != nums[i-1]:
                res = self.twoSum(i, nums, res)
        
        return res
        
    
    def twoSum(self, i, nums, res):
        
        lo, high = i+1, len(nums)-1
        
        while lo < high:
            
            tmp_sum = nums[i] + nums[lo] + nums[high]
                
            if tmp_sum > 0:
                high -= 1
            
            elif tmp_sum < 0:
                lo += 1
            
            else:
                res.append( [nums[i],nums[lo],nums[high]] )
                lo += 1
                high -= 1
                
                while( (lo < high) and nums[lo] == nums[lo-1]):
                    lo += 1
        return res

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        tmp_set = set()
        
        nums.sort()
        
        for i in range(0, len(nums)):
            
            start, end = i+1, len(nums)-1
            
            target = -nums[i]
            
            while start < end:
                
                if nums[start]+nums[end] == target:
                    
                    tmp_set.add((nums[i], nums[start], nums[end]))
                    start += 1
                    
                elif nums[start]+nums[end] < target:
                    start += 1
                    
                elif  nums[start]+nums[end] > target:
                    end -= 1
                    
        
        for x in tmp_set:
            res.append(list(x))
        
        return res
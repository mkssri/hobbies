#!/usr/bin/python3

# Leetcode Link - https://leetcode.com/problems/maximum-product-subarray/


from typing import List
import math

# Timelimit exceeded

"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product_subarray = -math.inf
        
        for i in range(0, len(nums)):
            
            tmp = 1
            
            for j in range(i, len(nums)):
                
                tmp *= nums[j]
                max_product_subarray = max(max_product_subarray, tmp)
        
        return max_product_subarray


#[2,1,3,4,5]

"""
Time Complexity - O(N)
Space Complexity - O(1)
"""

class Solution:

  def returnMaxSubArrayProduct(self, nums):
  
    if len(nums) == 0:
      return 0
  
    max_product_subarray, min_product_subarray  = nums[0], nums[0]
    res = max(nums)
    
    
    for i in range(1, len(nums)):
      
      curr = nums[i]
      
      # tmp_max_product_subarray will have tmp_max, max_product_subarray will have until previous element max
      tmp_max_product_subarray = max(curr, max_product_subarray*curr, min_product_subarray*curr)
      
      min_product_subarray = min(curr, max_product_subarray*curr, min_product_subarray*curr)
      
      max_product_subarray = tmp_max_product_subarray
      
      res = max(max_product_subarray, res)
    
    
    return res
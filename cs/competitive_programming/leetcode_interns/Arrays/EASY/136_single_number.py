#!/usr/bin/python3

# Link - https://leetcode.com/problems/single-number/

from typing import List
from collections import defaultdict

import math

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return None
        
        
        for x in nums:
        
            temp = nums.count(x)
            
            if temp == 1:
                return x

    # List Operation
    """
    TIME COMPLEXITY - O(N^2)
    SPACE COMPLEXITY - O(N)
    """  
    def singleNumberV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    # HASH Table
    """
    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(N)
    """  
    def singleNumberV2(self, nums: List[int]) -> int:
        
        hash_table_dict = defaultdict(int)
        
        for x in nums:
            hash_table_dict[x] += 1

        
        for i in hash_table_dict:
            
            if hash_table_dict[i] == 1:
                return i
            
        
    # Approach 3: Math
    """
    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(N)
    """  
    def singleNumberV3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    # Approach 4: BIT MANUPLATION
    """
    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(1)
    """  
    def singleNumberV4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0
        
        for x in nums:
            
            a ^= x
        
        return a
    
    
    
if __name__ == "__main__":
    
    obj = Solution()
    
    nums = [36,37,37,38,38,1,1]
    out = obj.singleNumberV4(nums)
    print(out)
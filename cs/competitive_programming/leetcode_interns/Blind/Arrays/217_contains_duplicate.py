#!/usr/bin/python3

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        set1 = set(nums)
        
        if len(set1) == len(nums):
            return False
        else:
            return True
        
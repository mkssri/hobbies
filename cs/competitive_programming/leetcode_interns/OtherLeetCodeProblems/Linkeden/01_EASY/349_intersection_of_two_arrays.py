#!/usr/bin/python3

# Link - https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    
        if len(nums1) >= len(nums2):
            small_lst, large_lst = nums2, nums1
        else:
            small_lst, large_lst = nums1, nums2
            
        out = []
        
        for x in small_lst:
            
            if x in large_lst:
                out.append(x)
        
        out = list(set(out))
        
        return out
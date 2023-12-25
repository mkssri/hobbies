#!/usr/bin/python3

# Link - https://leetcode.com/problems/container-with-most-water/

from typing import List

"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        for i in range(0, len(height)):
            
            for j in range(i+1, len(height)):
                
                length = j - i
                h = min(height[i], height[j])
                
                area = length * h
                
                max_area = max(area, max_area)
                
        
        return max_area


"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        i, j = 0, len(height)-1
        
        while(i<j):
            
            area = min(height[i], height[j]) * (j-i)
            max_area = max(max_area, area)
            
            
            if height[i] < height[j]:
                i += 1
            else:
                j = j-1
        
        return max_area
#!/usr/bin/python3

# Link - https://leetcode.com/problems/container-with-most-water/

import math
from typing import List

"""
# BRUTE FORCE METHOD
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        len_height = len(height)
        
        max_area = -math.inf
        
        for x in range(len_height):
            
            for y in range(x+1, len_height):
                
                area = (y-x)*min(height[x], height[y])
                max_area = max(max_area, area)
        
        return max_area
                

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        start,end = 0, len(height)-1
        
        while(start < end):
            
            max_area = max( max_area, (end-start)*min(height[end],height[start]) )
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return max_area
                
    
    
    
    


if __name__ == "__main__":
    
    print("OBJECT")

    obj = Solution()
    
    height = [1,8,6,2,5,4,8,3,7]
    out = obj.maxArea(height)
    print(out)
    
    height1 = [1,1]
    out1 = obj.maxArea(height1)
    print(out1)
    
    height2 = [4,3,2,1,4]
    out2 = obj.maxArea(height2)
    print(out2)
    
    height3 = [1,2,1]
    out3 = obj.maxArea(height3)
    print(out3)

    print("OBJECT1")
    obj1 = Solution1()
    
    height = [1,8,6,2,5,4,8,3,7]
    out = obj1.maxArea(height)
    print(out)
    
    height1 = [1,1]
    out1 = obj1.maxArea(height1)
    print(out1)
    
    height2 = [4,3,2,1,4]
    out2 = obj1.maxArea(height2)
    print(out2)
    
    height3 = [1,2,1]
    out3 = obj1.maxArea(height3)
    print(out3)
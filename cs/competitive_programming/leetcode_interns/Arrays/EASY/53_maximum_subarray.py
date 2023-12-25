#!/usr/bin/python3

from typing import List
import math

# Time limit exceeded
"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(N)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum, i = nums[0], 0
        
        for i in range(len(nums)+1):
            
            for j in range(i+1,len(nums)+1):
                
                tst_lst = nums[i:j]
                # print(tst_lst)
                lst_sum = self.calcSum(tst_lst)
                
                if lst_sum > max_sum:
                    max_sum = lst_sum
        return max_sum             
    
    def calcSum(self, lst):
        return sum(lst)

# Time limit exceeded
"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_subarray = -math.inf
        
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i,len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray



# Dynamic Programming
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
Whenever you see a question that asks for the maximum or minimum of something, 
consider Dynamic Programming as a possibility. 
"""
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray



if __name__ == "__main__":
    
    # Solution
    obj1 = Solution()
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    out = obj1.maxSubArray(nums1)
    print(out)
    
    nums2 = [1]
    out = obj1.maxSubArray(nums2)
    print(out)
    
    nums3 = [5,4,-1,7,8]
    out = obj1.maxSubArray(nums3)
    print(out)

    # Solution 1
    obj1 = Solution1()
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    out = obj1.maxSubArray(nums1)
    print(out)
    
    nums2 = [1]
    out = obj1.maxSubArray(nums2)
    print(out)
    
    nums3 = [5,4,-1,7,8]
    out = obj1.maxSubArray(nums3)
    print(out)

    # Solution 2
    obj1 = Solution2()
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    out = obj1.maxSubArray(nums1)
    print(out)
    
    nums2 = [1]
    out = obj1.maxSubArray(nums2)
    print(out)
    
    nums3 = [5,4,-1,7,8]
    out = obj1.maxSubArray(nums3)
    print(out)
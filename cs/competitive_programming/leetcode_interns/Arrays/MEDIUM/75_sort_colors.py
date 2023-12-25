#!/usr/bin/python3


from typing import List

"""
Time Complexity - O(N*LOG(N)) 
Space Complexity - O(1)
"""     
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        return nums.sort()

"""
Time Complexity - O(N) 
Space Complexity - O(N)
"""           
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        colors_dict, res = {}, []
        
        for x in nums:
            
            if x not in colors_dict.keys():
                colors_dict[x] = 1
            elif x in colors_dict.keys():
                colors_dict[x] += 1
        
        
        for x in list(range(0,3)):
            
            if x in colors_dict.keys():
                res = res + [int(x)]*colors_dict[x]
        

        for x in range(0, len(res)):
            nums[x] = res[x]
            
        return nums
        
   
"""
Time Complexity - O(N) 
Space Complexity - O(1)
"""     
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # In nums[x], x < p0 => nums[p0] = 0 
        # In nums[x], x > p2 => nums[p2] = 2
        # Rest nums[x] = 1 
        
        p0 = curr = 0 
        p2 = len(nums)-1
        
        while curr <= p2:
            
            if nums[curr] == 0:
                
                nums[p0],nums[curr] = nums[curr],nums[p0]
                p0 += 1
                curr += 1
            
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
                
            
            
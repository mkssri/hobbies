#!/usr/bin/python3

from typing import List

# BRUTE FORCE METHOD
"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
               if nums[i]+nums[j] == target:
                   return [i,j]
                   
#Approach 2: Two-pass Hash Table
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_dict = {}
        
        # hash_dict = {key - nums[i] and value - i}
        
        for i in range(len(nums)):
            hash_dict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hash_dict.keys() and hash_dict.get(complement)!= i:
                
                return [i, hash_dict.get(complement)]
            
        
        
        print(hash_dict)
        
        
if __name__ == "__main__":
    
    obj = Solution()
    nums, target = [2,7,11,15], 9
    
    out = obj.twoSum(nums, target)
    print(out)
    
    obj1 = Solution1()
    nums1, target1 = [2,7,11,15], 9
    
    out = obj1.twoSum(nums1, target1)
    print(out)
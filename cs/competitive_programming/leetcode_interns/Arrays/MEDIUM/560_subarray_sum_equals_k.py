#!/usr/bin/python3

#Link - https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            
            sub_array_sum = 0
            
            for j in range(i, len(nums)):
                sub_array_sum += nums[j]
    
                if sub_array_sum == k:
                    
                    count += 1        
        
        
        return count
    
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count, sum = 0, 0
        tst_dict = {}

        tst_dict[0] = 1
        
        for i in range(len(nums)):
            sum += nums[i]
            
            if (sum-k) in tst_dict.keys():
                """
                why adding ? -> tst_dict.get(sum-k) since already these many entries there
                so new sum-k can be acheived by subtracting current sum with any of the already existing
                tst_dict.get(sum-k)
                """
                count += tst_dict.get(sum-k)
            
            # TERNARY OPERATOR  
            tst_dict[sum] = tst_dict[sum]+1 if sum in tst_dict.keys() else 1
            
            # if sum in tst_dict.keys():
            #     tst_dict[sum] += 1
            # else:
            #     tst_dict[sum] = 1
        
        return count
    
    
    
    
    
if __name__ == "__main__":
    
    obj = Solution()
    
    nums, k = [1,1,1], 2
    out = obj.subarraySum(nums, k)
    print(out)
    
    nums, k  = [1,2,3], 3
    out = obj.subarraySum(nums, k)
    print(out)


    obj1 = Solution1()
    
    nums, k = [1,1,1], 2
    out = obj1.subarraySum(nums, k)
    print(out)
    
    nums, k  = [1,2,3], 3
    out = obj1.subarraySum(nums, k)
    print(out)
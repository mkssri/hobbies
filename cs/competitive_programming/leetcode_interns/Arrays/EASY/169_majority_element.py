#!/usr/bin/python3

from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority_count = len(nums)/2
        
        set_list = list(set(nums))
        
        for x in set_list:            
            count1 = nums.count(x)
            if count1 > majority_count:
                return x
# HASHMAP
class Solution1:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        print(counts)
        print(max(counts.keys(), key=counts.get))
        return max(counts.keys(), key=counts.get)
    
# Sorting
class Solution2:
    def majorityElement(self, nums):
        
        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    nums = [3,2,3]
    obj1 = Solution1()
    out = obj1.majorityElement(nums)
    
    print(out)
    
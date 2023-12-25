#!/usr/bin/python3

# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)-1

        while start <= end:

            mid = (start+end)//2
            # mid = start + (end-start)//2


            if nums[mid] == target:
                return mid

            # Mid in Left

            if nums[mid] >= nums[start]:

                if target > nums[mid] or target < nums[start]:
                    start = mid+1
                else:
                    end = mid-1
                
            # Mid in Right
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid-1
                else:
                    start = mid+1

        return -1


obj = Solution()
# nums, target = [4,5,6,7,0,1,2], 0
# out = obj.search(nums, target)
# print(out)

# nums, target = [4,5,6,7,0,1,2], 3
# out = obj.search(nums, target)
# print(out)

nums, target = [1], 0
out = obj.search(nums, target)
print(out)
#!/usr/bin/python3

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:

    def minInRotatedSortedArray(self, nums):
        
        res = nums[0]
        start, end = 0, len(nums)-1


        while start <= end:

            #BASE CASE
            if nums[start] <= nums[end]:
                res = min(res, nums[start])
                break


            mid = (start+end)//2
            res = nums[mid]


            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid-1
        return res




obj = Solution()
nums = [2,3,4,5,1]
out = obj.minInRotatedSortedArray(nums)

print(out)

nums = [1,2,3,4,5]
out = obj.minInRotatedSortedArray(nums)

print(out)


nums = [4,5,1,2,3]
out = obj.minInRotatedSortedArray(nums)

print(out)

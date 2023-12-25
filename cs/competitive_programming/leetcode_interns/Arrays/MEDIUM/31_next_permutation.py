#!/usr/bin/python3

# Link - https://leetcode.com/problems/next-permutation/

# Solution Youtube Link - https://www.youtube.com/watch?v=9xT2Xzlo4i4&t=617s

from typing import List

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""
class Solution:
    
    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp
        
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
    
    

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        if len(nums) == 1:
            return
        
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        
        dec = len(nums) - 2
        
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec -= 1
        
        self.reverse(nums, dec+1, len(nums)-1)

        """
        If full list is in descending order following if block will be executed
        since dec will be -1 as above while loop was fully reversed so it will change from
        decending order to the ascending order.
        """
        if dec == -1:
            return
        
        next_num = dec + 1

        
        while next_num <= len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
            
        self.swap(nums, next_num, dec)
        

    



if __name__ == "__main__":
    obj = Solution()
    
    nums = [1,2,3]
    out = obj.nextPermutation(nums)
    print(out)
    
    nums1 = [3,2,1]
    out1 = obj.nextPermutation(nums1)
    print(out1)
    
    # nums2 = [1,1,5]  
    # out2 = obj.nextPermutation(nums2)
    # print(out2)
    
    nums = [1,2]
    out = obj.nextPermutation(nums)
    print(out)
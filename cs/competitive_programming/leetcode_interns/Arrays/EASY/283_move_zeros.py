#!/usr/bin/python3

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        ans = []
        
        for x in nums:
            if x != 0:
                ans.append(x)
        
        while(zero_count > 0):
            ans.append(0)
            zero_count -= 1
        
        for i in range(0,len(nums)):
            nums[i] = ans[i]    
        
        print(nums)
        
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        
        for x in range(0, len(nums)):
        
            if nums[x] != 0:
                nums[lastNonZeroFoundAt], nums[x] = nums[x], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
                
        return nums
                


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    # obj1 = Solution()
    # out = obj1.moveZeroes(nums)
    obj2 = Solution1()
    out = obj2.moveZeroes(nums)
    print(out)
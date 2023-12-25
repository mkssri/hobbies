#!/usr/bin/python3

# Link - https://leetcode.com/problems/3sum/

from typing import List

"""
# BRUTE FORCE METHOD
TIME COMPLEXITY - O(N^3)
SPACE COMPLEXITY - O(1)

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        len_nums = len(nums)

        # EDGE CASE
        if len_nums == 0 or nums == [0] or nums == [0,0]:
            return []
        
        for x in range(len_nums):
            for y in range(x+1,len_nums):
                for z in range(y+1,len_nums):
                    
                    sum = nums[x] + nums[y] + nums[z]
                    
                    if sum == 0:
                        
                        if [ nums[x], nums[y], nums[z] ] not in res and \
                            [ nums[x], nums[z], nums[y] ] not in res and \
                            [ nums[y], nums[x], nums[z] ] not in res and \
                            [ nums[y], nums[z], nums[x] ] not in res and \
                            [ nums[z], nums[x], nums[y] ] not in res and \
                            [ nums[z], nums[y], nums[x] ] not in res:
                                
                            res.append( [ nums[x], nums[y], nums[z] ] )

        return res

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""  

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        len_nums = len(nums)

        # EDGE CASE
        if len_nums == 0 or nums == [0] or nums == [0,0]:
            return []
        
        for x in range(len_nums):
            for y in range(x+1,len_nums):
                    
                    sum = nums[x] + nums[y]
                    z = -1*sum
                    
                    if z in nums[y+1:len_nums]:
                        if [ nums[x], nums[y], z ] not in res and \
                            [ nums[x], z, nums[y] ] not in res and \
                            [ nums[y], nums[x], z ] not in res and \
                            [ nums[y], z, nums[x] ] not in res and \
                            [ z, nums[x], nums[y] ] not in res and \
                            [ z, nums[y], nums[x] ] not in res:
                                
                            res.append( [ nums[x], nums[y], z ] )

        return res

"""
Time Complexity - O(N^2) => Two Sum II is O(N) and we calling N times so it is O(N^2) and sorting the array takes O(nlogn). So, overall complexity
is O(N^2 + NlogN) = O(N^2)

Space Complexity - from O(logN) to O(N), depending on the implementation of the sorting algorithm. 
For the purpose of complexity analysis, we ignore the memory required for the output. 
"""
       
        
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSumII(nums, i, res)
                
        return res
                
    
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        
        lo, hi = i+1, len(nums)-1
        
        while(lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while(lo < hi and nums[lo]==nums[lo-1]):
                    lo += 1

if __name__ == "__main__":
    
    # #OBJECT
    # obj = Solution()
    
    # nums = [-1,0,1,2,-1,-4]
    # out = obj.threeSum(nums)
    # print(out)
    
    # nums1 = []
    # out1 = obj.threeSum(nums1)
    # print(out1)

    # nums2 = [0]
    # out2 = obj.threeSum(nums2)
    # print(out2)
    
    # #OBJECT1

    # obj1 = Solution1()
    
    # nums = [-1,0,1,2,-1,-4]
    # out = obj1.threeSum(nums)
    # print(out)
    
    # nums1 = []
    # out1 = obj1.threeSum(nums1)
    # print(out1)

    # nums2 = [0]
    # out2 = obj1.threeSum(nums2)
    # print(out2)

    #OBJECT2

    obj2 = Solution2()
    
    nums = [-1,0,1,2,-1,-4]
    out = obj2.threeSum(nums)
    print(out)
    
    nums1 = []
    out1 = obj2.threeSum(nums1)
    print(out1)

    nums2 = [0]
    out2 = obj2.threeSum(nums2)
    print(out2)
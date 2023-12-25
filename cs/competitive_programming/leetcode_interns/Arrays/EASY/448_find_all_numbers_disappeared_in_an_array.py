#!/usr/bin/python3

from typing import List

# Did not work (Time Limit Exceeded!)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        out_lst = list(range(1,n+1))

        nums = list(set(nums))
        
        for x in nums:
            out_lst.remove(x)
            
        return out_lst    
    

# HASH TABLE WORKED
"""
Time Complexity : O(N)
Space Complexity : O(N)
"""
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:       
        hash_table = {}
        
        for num in nums:
            hash_table[num] = 1
        
        result = []
        
        for x in range(1, len(nums)+1):
            
            if x not in hash_table:
                result.append(x)
        
        return result
    
# SPACE in Place modification solution
"""
Time Complexity : O(N)
Space Complexity : O(1)
"""
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:       
 
        
        for i in range(len(nums)):
            
            new_index = abs(nums[i]) - 1
            
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        result = []
        
        for i in range(1, len(nums)+1):
            
            if nums[i-1] > 0:
                result.append(i)
                
        return result    

if __name__ == "__main__":
    obj1 = Solution()
    nums1 = [4,3,2,7,8,2,3,1]
    out = obj1.findDisappearedNumbers(nums1)
    print(out)
    
    nums2 = [1,1]
    out = obj1.findDisappearedNumbers(nums2)
    print(out)

    obj2 = Solution1()
    nums1 = [4,3,2,7,8,2,3,1]
    out = obj2.findDisappearedNumbers(nums1)
    print(out)
    
    nums2 = [1,1]
    out = obj2.findDisappearedNumbers(nums2)
    print(out)

    obj3 = Solution2()
    nums1 = [4,3,2,7,8,2,3,1]
    out = obj3.findDisappearedNumbers(nums1)
    print(out)
    
    nums2 = [1,1]
    out = obj3.findDisappearedNumbers(nums2)
    print(out)
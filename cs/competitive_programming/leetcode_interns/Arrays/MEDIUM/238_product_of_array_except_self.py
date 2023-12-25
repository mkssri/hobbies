#!/usr/bin/python3

# Link - https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for x in range(len(nums)):
            tmp = self.productOut(nums, x)
            res.append(tmp)
            
        return res
    
    def productOut(self, nums, i):
        
        tmp = 1
        
        if 0 in nums and nums[i] != 0:
            return 0
        
        for x in range(len(nums)):
            if x == i:
                continue
            else:
                tmp *= nums[x]
        return tmp

"""
TIME Complexity - O(N)
Space Complexity - O(N)
"""
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: For the element at index '0', there are no elements to the left
        # so the L[0] would be 1
        
        L[0] = 1
        
        for i in range(1,length):
            # L[i-1] already contains the product of the elements to the left of 'i-1'
            # Simply multiplying it with nums[i-1] would give the product of all
            # elements to the left of index 1
            L[i] = nums[i-1] * L[i-1]
            
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length-1', there are no elements to the right,
        # so the R[length -1] would be 1
        R[length - 1] = 1
        
        for i in reversed(range(length-1)):
            # R[i+1] already contains the product of elements to the right of 'i+1'
            # Simply multiplying it with nums[i+1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i+1] * R[i+1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            
            answer[i] = L[i] * R[i]
            
        return answer            
            
    
"""
TIME Complexity - O(N)
Space Complexity - O(1)
"""
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array
        length = len(nums)
        
        # The answer to be returned
        answer = [0] * length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
            
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
            
  
 
if __name__ == "__main__":
    
    # obj = Solution()
    # nums = [1,2,3,4]
    # out = obj.productExceptSelf(nums)
    # print(out)

    obj = Solution1()
    nums = [1,2,3,4]
    out = obj.productExceptSelf(nums)
    print(out)

    obj = Solution2()
    nums = [1,2,3,4]
    out = obj.productExceptSelf(nums)
    print(out)
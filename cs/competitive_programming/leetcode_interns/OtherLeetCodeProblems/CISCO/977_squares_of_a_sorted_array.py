from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        left, right = 0, len(nums) - 1
        
        out = [0]*len(nums)
        index = right
        
        while left <= right:
            
            leftSq = pow(nums[left], 2)
            rightSq = pow(nums[right],2)
            
            if leftSq > rightSq:
                
                out[index] = leftSq
                index-= 1
                left += 1
                
            else:
                out[index] = rightSq
                index-= 1
                right -= 1
        
        return out
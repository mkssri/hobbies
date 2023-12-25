#!/usr/bin/python3

# Link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

        
class Solution:
    
    """
    TIME Complexity - O(N)
    SPACE Complexity - O(1)
    """
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low, high = 0, len(numbers)-1
        
        while(low < high):
            
            
            sum = numbers[low] + numbers[high]
            if (sum == target):
                return [low+1, high+1]
            elif sum < target:
                low += 1
            else:
                high -=1
        
        return [-1,-1]
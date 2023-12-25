#!/usr/bin/python3

# Link - https://leetcode.com/problems/kth-largest-element-in-an-array/
# Youtube Solution - https://www.youtube.com/watch?v=jZebUENDJ1U&t=304s


from typing import List
import random

"""
TIME COMPLEXITY - O(N*logN)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        tmp = sorted(nums, reverse=True)
        print(tmp[k-1])
        return tmp[k-1]

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""   

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            
        # QUICK SORT TYPE OF SOLUTION
        
        pivot_ele = random.choice(nums)
        print("random number choosed was - {}".format(pivot_ele))
        
        
        left = [x for x in nums if x > pivot_ele]
        right = [x for x in nums if x < pivot_ele]
        mid = [x for x in nums if x == pivot_ele]
        
        print("LEFT is {}".format(left))
        print("RIGHT is {}".format(right))
        print("MID is {}".format(mid))
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L+M:
            return self.findKthLargest(right, k-(L+M))
        else:
            # Caught the required element
            return mid[0]


        
        
    
    

if __name__ == "__main__":
    
    obj  = Solution1()
    
    
    nums = [-1, 2, 0]
    k = 2
    out = obj.findKthLargest(nums,k)
    print(out)
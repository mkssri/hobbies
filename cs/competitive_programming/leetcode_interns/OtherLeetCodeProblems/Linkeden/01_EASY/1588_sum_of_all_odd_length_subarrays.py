#!/usr/bin/python3

"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        result = 0
        
        for i in range(0,n):
            # Number subarrays starting with index i
            start = n - i

            # Number subarrays ending with index i
            end = i + 1

            # Total = start*end
            total = start*end
            
            # Odd length subarrays
            # if total is even then /2 else /2 + 1 
            odd = int(total/2)
            
            if total%2 != 0:
                odd += 1
            
            result += odd*arr[i]
        
        return result



obj = Solution()
arr = [1,4,2,5,3]
res = obj.sumOddLengthSubarrays(arr)

print("res is {}".format(res))
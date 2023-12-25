#!/usr/bin/python3

# Link - https://leetcode.com/problems/merge-intervals/

"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
USAGE=>
lambda arguments : expression
"""

from typing import List

class Solution:
    """
    Time Complexity - O(nlogn) => sorting complexity is nlogn and traverse complexity is n, so it is O(nlogn)
    Space Complexity - O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Argument is list but only take x[0] as trigger point to sort the array
        intervals.sort(key=lambda x: x[0])
        merged = []


        for interval in intervals:
            """
            if length of output merged list is empty or new interval start is greater than end of 
            last element in list then add element directly to output merged list.
            """
            if(len(merged) == 0 or merged[-1][1] < interval[0]):
                # ADD the intervals to the output merged list
                merged.append(interval)
            else:
                # UPDATE LAST ELEMENT in merged list
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

if __name__ == "__main__":
    
    obj = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    out = obj.merge(intervals)
    print(out)
    
    intervals1 = [[1,4],[4,5]]
    out = obj.merge(intervals1)
    print(out)
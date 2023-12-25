#!/usr/bin/python3

# Link - https://www.youtube.com/watch?v=kd5u3GEQkPY&t=186s

import math
from typing import List

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""

"""
# Important Idea!!!
To rotate matrix by 90 degree =>
# First take the transpose of the matrix
# Following reverse the rows of the matrix
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        
        # LOGIC to TAKE TRANSPOSE of a matrix
        
        for row in range(len(matrix)):
            
            for column in range(len(matrix[row])):
                
                if row < column:
                    matrix[row][column], matrix[column][row] =  matrix[column][row], matrix[row][column]         
                    
        # REVERSE Each row
        
        for i in range(len(matrix)):
            
            # INBUILT reverse function
            # matrix[i].reverse() 
            
            # Custom Function
            self.revLst(matrix[i])
    
    
    def revLst(self, lst):
        
        if len(lst) == 0 or len(lst) == 1:
            return lst
        
        start, end = 0, len(lst)-1
        
        while start <= end:
            
            lst[start], lst[end] = lst[end], lst[start]
            
            start += 1
            end -= 1

        return lst
    


if __name__ == "__main__":
    
    obj = Solution()
    
 
#!/usr/bin/python3

from typing import List


class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row_max = len(matrix)
        column_max = len(matrix[0])
        
        for row in range(row_max):
            for column in range(column_max):
                                
                i,j = row, column
                
                ele_val = matrix[row][column]
                
                while i<row_max and j<column_max:
                    
                    
                    if matrix[i][j] == ele_val:
                        pass
                    else:
                        return False
                    i += 1
                    j += 1
        
        return True


"""
TIME Complexity - O(M*N)
SPACE Complexity - O(1)
"""             
                
class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row_max = len(matrix)
        column_max = len(matrix[0])
        
        for row in range(row_max):
            for column in range(column_max):
                                
                i,j = row, column
                
                ele_val = matrix[row][column]
                
                if i+1 < row_max and j+1 < column_max:
                    
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
                else:
                    continue
        return True                    
                    
                
                
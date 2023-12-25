#!/usr/bin/python3

# Link - https://leetcode.com/problems/number-of-islands/

# Solution Youtube Link - https://www.youtube.com/watch?v=uDB5QXTqMn0

from typing import List

"""
TIME COMPLEXITY - O(N*M)
SPACE COMPLEXITY - O(1) 
SPACE COMPLEXITY Worst Case - O(N*M) 
"""

class Solution:
    
    def dfs(self, grid, row, column):
        
        # First Make the corresponding row,column to zero (where we found 1)
        grid[row][column] = 0
        # top, bottom, right and left
        lst_adj_islands = [(row-1,column), (row+1, column), (row, column+1), (row, column-1)]
        # print(lst_adj_islands)
        for row,column in lst_adj_islands:
            
            if row >= 0 and row < len(grid) and column >= 0 and column < len(grid[row]) \
            and grid[row][column] == "1":
                
                self.dfs(grid, row, column)
                

    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_of_islands = 0
        
        for row in range(len(grid)):
                        
            for column in range(len(grid[row])):
            
                    if grid[row][column] == '1':
                        print("parent row n column - ({},{})".format(row,column))
                        self.dfs(grid, row, column)
                        num_of_islands += 1
                        
                        
                        
        print("num_of_islands is {}".format(num_of_islands))
        return num_of_islands
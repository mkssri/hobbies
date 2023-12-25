from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        fresh,time=0,0
        q = deque()


        for row in range(rows):
            for col in range(cols):
                if(grid[row][col]==1):
                    fresh+=1
                if(grid[row][col]==2):
                    q.append((row,col))
        
        #BFS
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while(q and fresh>0):
            for i in range(len(q)):
                r,c = q.popleft()
                for x,y in directions:
                    new_row = r+x
                    new_col = c+y

                    if(new_row<0 or new_row==rows or new_col<0 or new_col==cols or grid[new_row][new_col]==2 or grid[new_row][new_col]==0 ):
                        continue
                    grid[new_row][new_col]=2
                    q.append((new_row,new_col))
                    fresh-=1
            time +=1
        
        if fresh>0:
            return -1
        else:
            return time
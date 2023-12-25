class Solution:
    
    def dfs(self, ele, r, c, grid):

        loop_over = [ (r,c+1), (r,c-1), (r-1,c), (r+1,c) ]

        for (r,c) in loop_over:
            if( r < len(grid) and r >=0 and c < len(grid[r]) and c >=0 ):
                ele = grid[r][c]
                
                if ele == "1":
                    grid[r][c] = "0"
                    self.dfs( ele, r, c, grid )
                

        

    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        for r in range( len(grid) ):
            for c in range( len(grid[r]) ):

                ele = grid[r][c]
                if ele == "1":
                    self.dfs( ele, r, c, grid )
                    res += 1
        return res

class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        R=len(grid)
        C=len(grid[R-1])
        res=0

        def dfs(r, c):
            traverse=[(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
            for r,c in traverse:
                if(r>=0 and r<R and c>=0 and c<C):
                    if grid[r][c]=="1":
                        grid[r][c]="0"
                        dfs(r,c)

        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1":
                    grid[r][c]="0"
                    dfs(r,c)
                    res+=1

        return res

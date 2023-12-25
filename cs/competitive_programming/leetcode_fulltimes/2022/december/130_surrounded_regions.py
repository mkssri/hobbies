class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R=len(board)
        C=len(board[R-1])
        
        ## reverse thinking
        # capture unsurronded regions

        def dfs(r,c):
            if((r<0 or c<0 or r==R or c==C or board[r][c]!="O")):
                return
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(R):
            for c in range(C):
                if (board[r][c]=="O" and (r in [0,R-1] or c in [0,C-1])):
                    dfs(r,c)

        #convert rest O to X
        for r in range(R):
            for c in range(C):
                if(board[r][c]=="O"):
                    board[r][c]="X"

        #convert T to O
        for r in range(R):
            for c in range(C):
                if(board[r][c]=="T"):
                    board[r][c]="O"
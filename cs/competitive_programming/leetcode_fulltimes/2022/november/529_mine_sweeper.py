class Solution:
    
    def getAdjacentMines( self, board, x, y ):
        numMines = 0
        for r in range(x-1, x+2):
            for c in range(y-1, y+2):
                
                if( r>=0 and r < len(board) and c>=0 and c<len(board[r]) and board[r][c] =="M" ):
                    numMines += 1
        return numMines


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board

        x,y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            numMines = self.getAdjacentMines(board, x, y)
            if numMines:
                board[x][y] = str(numMines)
            else:
                board[x][y] = 'B'
                for r in range(x-1,x+2):
                    for c in range(y-1, y+2):
                        if( r>=0 and r<len(board) and c>=0 and c<len(board[r]) and board[r][c]!='B' ):
                            self.updateBoard(board, [r,c] )
        
        return board
class TicTacToe:
    
    def __init__(self, n: int):
        self.board = [[ 0 for i in range(n) ] for j in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        r,c = row,col
        self.board[r][c] = player #player=1 or 2
        n = self.n

        def checkRow(r):
            for c in range(n):
                 if self.board[r][c] != player: return False
            return True 

        def checkCol(c):
            for r in range(n):
                 if self.board[r][c] != player: return False
            return True 
        
        def checkDiag():
            for d in range(n):
                 if self.board[d][d] != player: return False
            return True 
        
        def checkAntiDiag():
            for r in range(n):
                 if self.board[r][n-r-1] != player: return False
            return True 

        for r in range(n):
            if checkRow(r): return player

        for c in range(n):
            if checkCol(c): return player

        if checkDiag(): return player
        if checkAntiDiag(): return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TicTacToe:
    
    def __init__(self, n: int):
        self.rows = [ 0 for i in range(n) ]
        self.cols = [ 0 for i in range(n) ]
        self.diag = 0
        self.antiDiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        needed = n
        if  player==1:
            self.rows[row] += 1
            if self.rows[row]==needed: return player
            self.cols[col] += 1
            if self.cols[col]==needed: return player

            if row==col: 
                self.diag += 1
                if self.diag==needed: return player

            if row+col==(n-1): 
                self.antiDiag += 1
                if self.antiDiag==needed: return player
        else:
            self.rows[row] -= 1
            if self.rows[row]==-needed: return player
            self.cols[col] -= 1
            if self.cols[col]==-needed: return player

            if row==col: 
                self.diag -= 1
                if self.diag==-needed: return player

            if row+col==(n-1): 
                self.antiDiag -= 1
                if self.antiDiag==-needed: return player
        return 0



        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
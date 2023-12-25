class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRows():
            for r in range(9):
                data = ""
                for c in range(9):
                    if board[r][c] not in data:
                        data += str(board[r][c])
                    elif board[r][c] != '.':
                        return False
            return True
        
        def checkCols():
            for c in range(9):
                data = ""
                for r in range(9):
                    if board[r][c] not in data:
                        data += str(board[r][c])
                    elif board[r][c] != '.':
                        return False
            return True

        
        def checkArrs():
            for r in range(0,9,3):
                for c in range(0,9,3):
                    data = ""
                    for r1 in range(3):
                        for c1 in range(3):
                            if board[r+r1][c+c1] not in data:
                                data += str(board[r+r1][c+c1])
                            elif board[r+r1][c+c1] != '.':
                                return False

            return True
                            
        
        if checkRows() and checkCols() and checkArrs():
            return True
        return False
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        data = []
        #flatten the board into an 1-d array.
        for row in board:
            data = data + row
        #use list's slice operation to get rows and columns
        for i in range(9):
            temp = data[9*i:9*(i+1)]
			#consider only digits
            temp = [elem for elem in temp if elem!="."]
            #use set to determine the existence of duplicates
            if len(temp)!=len(set(temp)):
                return False
            temp = data[i::9]
            temp = [elem for elem in temp if elem!="."]
            if len(temp)!=len(set(temp)):
                return False
        #get 3x3 subboard
        for i in range(0,9,3):
            for j in range(3):
                temp = data[i*9+j*3:i*9+(j+1)*3] + data[(i+1)*9+j*3:(i+1)*9+(j+1)*3] + \
                        data[(i+2)*9+j*3:(i+2)*9+(j+1)*3]
                temp = [elem for elem in temp if elem!="."]
                if len(temp)!=len(set(temp)):
                    return False
                    
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        def checkRow():
            for r in range(9):
                data=""
                for c in range(9):
                    ele=board[r][c]
                    if ele not in data:
                        data+=ele
                    elif ele != ".":
                        return False
            return True
        
        def checkCol():
            for c in range(9):
                data=""
                for r in range(9):
                    ele=board[r][c]
                    if ele not in data:
                        data+=ele
                    elif ele != ".":
                        return False
            return True


        def checkBlock():
            
            for r in range(0,9,3):
                for c in range(0,9,3):
                    data=""
                    for r1 in range(3):
                        for c1 in range(3):
                            ele=board[r+r1][c+c1]
                            if ele not in data:
                                data += ele
                            elif ele != ".":
                                return False
            return True

        
        if checkRow() and checkCol() and checkBlock():
            return True
        return False

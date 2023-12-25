#!/usr/bin/python3
import math

from typing import List

class Solution:
    def exist(self, board: List[List[str]], words: List[str]) -> List[bool]:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        out = []

        for y in range(len(words)):
            print("word is - {}".format(words[y]))
            for row in range(self.rows):
                for col in range(self.cols):
                    
                    if self.backtrack(row, col, words[y]):
                        out.append(True)
                        
            if len(out) == y+1:
                continue
            else:
                out.append(False)
        
        return out
    
    def backtrack(self, row, col, suffix):
        
        #bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True
        
        #check the current status, before jumping into backtracking
        if row < 0 or row == self.rows or col < 0 or col == self.cols \
         or self.board[row][col] != suffix[0]:
            return False
        
        ret = False
        
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        
        #explore 4 neighbour directons
        
        for rowOffset, colOffset in [(0,1), (1,0), (0,-1), (-1,0)]:
            ret = self.backtrack(row+rowOffset, col+colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret:
                break
        
        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]
        
        # Tried all directions, and did not find any match
        return ret
                
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

# https://www.youtube.com/watch?v=asbcE9mZz_U
class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()


        def dfs(r, c, node, word):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or \
                (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)


            
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # return list(res)

        out = []

        for x in words:
            if x in list(res):
                out.append(True)
            else:
                out.append(False)
        
        return out

        






if __name__ == "__main__":

    obj1 = Solution()

    board = [["D","O","G","P"],["C","A","T","Q"],["P","I","G","R"]]
    words = ["DOG","CAT","PIG", "Murali"]



    out = obj1.exist(board, words)
    print(out)

    obj2 = Solution1()
    board = [["D","O","G","P"],["C","A","T","Q"],["P","I","G","R"]]
    words = ["DOG","CAT","PIG", "Murali","DCP","OAT"]

    out = obj2.findWords(board, words)
    print(out)





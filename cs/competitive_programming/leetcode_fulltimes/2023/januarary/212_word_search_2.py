class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    # def get_root(self):
    #     return self.root

    def add_word(self,word):
        curr=self.root
        # curr=self.get_root()
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.end=True
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        obj=Trie()
        for word in words:
            obj.add_word(word)

        R=len(board)
        C=len(board[R-1])

        res,visit = set(),set()

        def dfs(r,c,node,word):

            if (r<0 or r==R or c<0 or c==C or (r,c) in visit 
                or board[r][c] not in node.children):
                return

            visit.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.end:
                res.add(word)
    
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))


        for r in range(R):
            for c in range(C):
                dfs(r,c,obj.root,"")

        return list(res)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        Trie=lambda: collections.defaultdict(Trie)
        root=Trie()
        res=[]

        def add_word(s):
            curr=root
            for c in s:
                curr=curr[c]
            curr['$']=s

        for word in words:
            add_word(word)
        
        R=len(board)
        C=len(board[R-1])

        def dfs(r,c,node):      
            ch=board[r][c]
            curr=node.get(ch)

            if not curr:
                return
            
            if '$' in curr:
                res.append(curr['$'])
                del curr['$']
            
            board[r][c]="#"

            if r>0: dfs(r-1,c,curr)
            if r<R-1: dfs(r+1,c,curr)
            if c>0: dfs(r,c-1,curr)
            if c<C-1: dfs(r,c+1,curr)

            board[r][c]=ch


        for r in range(R):
            for c in range(C):
                dfs(r,c, root)

        return res
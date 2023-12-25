class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end=True
        
    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i>=len(word):
                return node.end
            
            if word[i]==".":
                for child in node.children:
                    if dfs(node.children[child],i+1):
                        return True
            
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False
        return dfs(self.root,0)
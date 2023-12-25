class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False



class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end_of_word=True
        

    def search(self, word: str) -> bool:
        cur=self.root

        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.end_of_word 
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True

        

class TrieNode:

    def __init__(self):
        self.val = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.val:
                curr.val[c] = TrieNode()
            curr = curr.val[c]

        curr.end = True
        
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.val:
                curr = curr.val[c]
            else:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if c in curr.val:
                curr = curr.val[c]
            else:
                return False

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

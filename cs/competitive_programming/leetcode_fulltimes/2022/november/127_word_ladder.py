class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        # wordList.append(beginWord)

        
        # Making Adjacency list
        # we will get list of words that differ by one word
        adj_store = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                adj_store[pattern].append(word)
        
        res = 1
        #Do BFS
        visited_set = set()
        visited_set.add(beginWord)
        q = collections.deque([beginWord])

        while q:
            lvl_len = len(q)
            for _ in range(lvl_len):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i]+'*'+word[i+1:]
                    for neiWord in adj_store[pattern]:
                        if neiWord not in visited_set:
                            visited_set.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0
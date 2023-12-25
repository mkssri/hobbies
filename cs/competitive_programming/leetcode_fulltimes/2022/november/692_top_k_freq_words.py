class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # words.sort()

        count = {}

        for word in words:
            count[word] = count.get(word, 0)+1
        
        freq = []
        for i in range(1,len(words)+1):
            freq.append([])

        for k_c, v in count.items():
            freq[v].append(k_c)

        for lst in freq:
            lst.sort()
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res)==k:
                    return res
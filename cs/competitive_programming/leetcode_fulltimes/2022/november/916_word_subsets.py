class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def retCnt( word ):

            store=collections.defaultdict(lambda: 0)
            for c in word:
                store[c] += 1

            return store.items()
        
        def cmpAndReturn( lst1, lst2 ):

            for idx in range(len(lst1)):
                if(lst1[idx]<lst2[idx]):
                    return False
            return True
        
        def makeLst(word_tup):
            res = [0]*26
            for (k,v) in word_tup:
                idx = ord(k)-ord('a')
                res[idx] = v
            return res

        words2_lst = [0]*26

        for word in words2:
            word_tup = retCnt(word)

            for (k,v) in word_tup:
                idx = ord(k)-ord('a')
                words2_lst[idx] = max(words2_lst[idx], v)

        out = []
        for word in words1:
            word_tup = retCnt(word)
            res = makeLst(word_tup)

            if(cmpAndReturn(res,words2_lst)):
                out.append(word)
        
        return out
    

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        countB = Counter()
        # add only max to countB
        for b in words2:
            tempB = Counter(b)
            for i,v in tempB.items():
                if v > countB[i]:
                    countB[i] = v
        output = []
        # iterate through A
        for a in words1:
            tempA = Counter(a)
            isUniversal = True
            for k,v in countB.items():
                if v > tempA[k]:
                    isUniversal = False
            if isUniversal: output.append(a)
        
        return output
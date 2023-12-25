class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = collections.defaultdict(list)

        for s in strs:
            str_key = [0]*26

            for c in s:
                idx = ord(c)-ord("a")
                str_key[idx] += 1

            res[tuple(str_key)].append(s)

        
        return res.values()
    
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = collections.defaultdict(list)

        for s in strs:
            str_key = list(s)
            str_key.sort()
            str_key = tuple(str_key)

            res[str_key].append(s)

        return res.values()
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)
        for ele in strs:
            tmp = [0]*26
            cnt = 0
            while(cnt<len(ele)):
                tmp[ord(ele[cnt])-ord('a')]+=1
                cnt+=1
            store[tuple(tmp)].append(ele)
        
        return store.values()
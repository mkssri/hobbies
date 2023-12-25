class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash1 = [0]*26
        hash2 = [0]*26

        for c in s:
            hash1[ord(c)-ord('a')] += 1
        for c in t:
            hash2[ord(c)-ord('a')] += 1

        return hash1==hash2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        d1 = collections.defaultdict(int)

        for c in s:
            d1[c] += 1
        for c in t:
            d1[c] -= 1

        for v in d1.values():
            if(v<0 or v>0):
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        out = [0]*26

        for c in s:
            k = ord(c)-ord('a')
            out[k] +=1
        for c in t:
            k = ord(c)-ord('a')
            out[k] -=1
        for v in out:
            if(v<0 or v>0):
                return False
        return True 

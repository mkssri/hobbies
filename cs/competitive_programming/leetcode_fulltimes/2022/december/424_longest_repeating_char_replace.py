class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = {}
        res = 0
        left = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            while((right-left+1)-max(counter.values())>k):
                counter[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
        
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = {}
        res = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_freq = max(max_freq,counter[s[right]])

            while((right-left+1)-max_freq>k):
                counter[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
        
        return res
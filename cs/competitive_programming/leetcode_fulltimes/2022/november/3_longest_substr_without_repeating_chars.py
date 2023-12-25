class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lenLongSubStr = 0

        for idx in range( len(s) ):
            subStr = s[idx]
            for nxtIdx in range( idx+1, len(s) ):
                ele = s[nxtIdx]
                if ele not in subStr:
                    subStr += ele
                else:
                    break
            lenLongSubStr = max(lenLongSubStr, len(subStr))
        
        return lenLongSubStr
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        l = 0
        res = 0
        for r in range( len(s) ):
            ele = s[r]

            while ele in char_set:
                left_ele = s[l]
                char_set.remove(left_ele)
                l += 1

            char_set.add(ele)
            res = max( res, r-l+1 )

        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right-left+1)
        return res

#!/usr/bin/python3

# Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            
            tst_str = ""
            
            for j in range(i, len(s)): 
                if s[j] not in tst_str:
                    tst_str += s[j]
                    count = max(count, len(tst_str))
                else:
                    break
        return count
                


if __name__ == "__main__":
    
    obj = Solution()
    s = "murali"
    out = obj.lengthOfLongestSubstring(s)
    print(out)
    
    s = "abcabcbb"
    out = obj.lengthOfLongestSubstring(s)
    print(out)
    
    s = "bbbbb"
    out = obj.lengthOfLongestSubstring(s)
    print(out)
    
    s = "pwwkew"
    out = obj.lengthOfLongestSubstring(s)
    print(out)

    s = ""    
    out = obj.lengthOfLongestSubstring(s)
    print(out)
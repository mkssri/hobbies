#!/usr/bin/python3

# Q - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Youtube Ans - https://www.youtube.com/watch?v=wiGpQwVHdE0

"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        
        l = 0
        res = 0
        
        for r in range(len(s)):
            
            while s[r] in char_set:
                
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            
            res  = max(res, r-l+1)
        
        return res
                
"""
Time Complexity - O(N^2)
Space Complexity - O(N)
"""

class Solution1:
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
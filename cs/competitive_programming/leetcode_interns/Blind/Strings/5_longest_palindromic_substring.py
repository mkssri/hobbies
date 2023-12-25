#!/usr/bin/python3

"""
Time Complexity - O(N^3)
Space Complexity - O(N)
"""

# Time limit Exceeded

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        out_str = ""
        
        for i in range(0, len(s)):
            
            for j in range(i, len(s)):
                
                if self.isPalindrome(s[i:j+1]):
                    
                    if len(s[i:j+1]) >  len(out_str):
                        out_str = s[i:j+1]
                
        return out_str
    
    
    def isPalindrome(self, s):
        
        i,j = 0,len(s)-1
        
        while i < j:
            
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        
        return True

"""
Time Complexity - O(N^2)
Space Complexity - O(N)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_str = ""
        
        for x in range(0, len(s)):
            
            # odd substring
            odd_str = self.maxString(s, x, x)
                    
            # even substring
            even_str = self.maxString(s, x, x+1)
            
            if len(even_str) >= len(odd_str):
                
                if len(even_str) > len(max_str):
                    max_str = even_str  
                
            else:
                if len(odd_str) > len(max_str):
                    max_str = odd_str
        
        return max_str
    
    
    def maxString(self, s, i, j):
        
        while i >=0 and j < len(s) and s[i] == s[j]:
            
            i -= 1
            j += 1
        
        return s[i+1:j]
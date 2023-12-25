#!/usr/bin/python3

# https://leetcode.com/problems/valid-palindrome-ii/

"""
Input: s = "aba"
Output: true
"""

"""
# Brute Force Solution - 
Time Complexity - O(n^2)
Space Complexity - O(n)
"""

class Solution1:
    def validPalindrome(self, s: str) -> bool:
        
        if self.toCheckPalindrome(s):
            return True
        
        for x in range(0,len(s)):
            
            temp_str = s[:x]+s[x+1:]
            
            if self.toCheckPalindrome(temp_str):
                return True
        
        return False
            
            
        
    
    def toCheckPalindrome(self, s):
        
        len_s = len(s)
        mid_s = len_s//2
        
        # EVEN
        if  len_s%2 == 0:
            i,j = mid_s-1, mid_s
        
        # ODD
        else:
            i,j = mid_s-1, mid_s+1
        
        while i >= 0 and j <= len_s-1:
            
            if s[i] == s[j]:
                
                i -= 1
                j += 1
                continue
                
            else:
                
                return False
        
        
        return True

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""

class Solution2:
    def validPalindrome(self, s: str) -> bool:

        i, j = 0, len(s)-1
        
        while(i<j):
            
            if s[i] != s[j]:
                
                return self.isPalindrome(s,i+1,j) or self.isPalindrome(s,i,j-1)
            
            i += 1
            j -= 1
    
        return True
    
    def isPalindrome(self, s, i , j):
        
        while(i < j):
            
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
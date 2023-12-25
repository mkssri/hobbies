#!/usr/bin/python3

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for x in range(len(s)):
            count += self.countPali(s, x, x)
            
            count += self.countPali(s, x, x+1)
            
        return count
    
    def countPali(self, s, i, j):
        
        count = 0
        
        while i >= 0 and j < len(s) and s[i] == s[j]:
            
            count += 1
            i -= 1
            j += 1
            
        return count
                

"""
TIME COMPLEXITY - O(N^3)
SPACE COMPLEXITY - O(N)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(0,len(s)):
            
            tmp_str = ""
            
            for j in range(i, len(s)):
                
                tmp_str += s[j]
                
                if self.checkPalindrome(tmp_str):
                    count += 1

        return count
                    
    def checkPalindrome(self, tmp_str):
        
        i, j = 0, len(tmp_str)-1
        
        while(i < j):
            
            if tmp_str[i] == tmp_str[j]:
                i += 1
                j -= 1
            else:
                return False
            
        return True

"""
TIME COMPLEXITY - O(N^3)
SPACE COMPLEXITY - O(1)
"""             
class Solution1:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(0,len(s)):
            
            for j in range(i, len(s)):
                
                if self.checkPalindrome(s[i:j+1]):
                    count += 1

        return count
                    
    def checkPalindrome(self, tmp_str):
        
        i, j = 0, len(tmp_str)-1
        
        while(i < j):
            
            if tmp_str[i] == tmp_str[j]:
                i += 1
                j -= 1
            else:
                return False
            
        return True
                
                
                
                
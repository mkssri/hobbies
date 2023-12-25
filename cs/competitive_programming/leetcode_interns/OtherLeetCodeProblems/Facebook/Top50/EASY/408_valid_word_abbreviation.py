#!/usr/bin/python3

#  Problem - https://leetcode.com/problems/valid-word-abbreviation/




"""
Time Complexity - O(N)
Space Complexity - O(1)
"""



class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:      
        
        p, q = 0, 0
        
        while ( p < len(word) and q < len(abbr)):
            
            
            if word[p] == abbr[q]:
                
                p+=1
                q+=1
                continue
            
            
            if not abbr[q].isnumeric() or abbr[q] == '0':
                return False
            
            if abbr[q].isnumeric():
                
                r = q
                
                while q < len(abbr) and abbr[q].isnumeric():
                    
                    q += 1
                
                num = abbr[r:q]
                
                p += int(num)
        
        return p == len(word) and q == len(abbr)
            
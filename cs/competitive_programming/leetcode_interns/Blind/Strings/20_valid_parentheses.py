#!/usr/bin/python3

# Link - https://leetcode.com/problems/valid-parentheses/


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_dict = {}
        valid_dict['('] = ')'
        valid_dict['{'] = '}'
        valid_dict['['] = ']'

        stk = []
        
        for x in s:
            
            if x in valid_dict.keys():
                
                stk.append(x)
            
            elif x in valid_dict.values() and len(stk) !=0 and x == valid_dict[stk.pop()]:
                continue
            
            else:
                return False
        
        return len(stk) == 0
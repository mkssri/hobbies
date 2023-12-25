#!/usr/bin/python3

# Link - https://leetcode.com/problems/valid-parentheses/

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        var_dict = {}
        var_dict['['] = ']'
        var_dict['{'] = '}'
        var_dict['('] = ')'

        
        len_s = len(s)
        
        if len_s % 2 != 0:
            return False
        
        stk = []
        
        for x in s:
            
            if x in var_dict.keys():
                stk.append(x)
            else:
                if len(stk) != 0 and x == var_dict[stk.pop()]:
                    continue
                else:
                    return False
        if len(stk) == 0:
            return True
        else:
            return False
    
    
    

if __name__ == "__main__":
    
    obj = Solution()
    
    s = "()"
    out = obj.isValid(s)
    print(out)
    
    s1 = "()[]{}"
    out1 = obj.isValid(s1)
    print(out1)
    
    s2 = "(]"
    out2 = obj.isValid(s2)
    print(out2)
    
    s3 = "([)]"
    out3 = obj.isValid(s3)
    print(out3)
    
    s4 = "{[]}"
    out4 = obj.isValid(s4)
    print(out4)
    
    s5 = "(("
    out5 = obj.isValid(s5)
    print(out5)
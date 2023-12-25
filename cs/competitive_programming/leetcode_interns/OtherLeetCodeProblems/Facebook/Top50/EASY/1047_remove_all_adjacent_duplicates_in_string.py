#!/usr/bin/python3

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/solution/
"""
TIME Complexity - O(N)
SPACE Complexity - O(N)
"""
class Solution1:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        
        for ch in S:

            if stk and ch == stk[-1]:
                stk.pop()
            else:
                stk.append(ch)

        
        return ''.join(stk)

"""
TIME Complexity - O(N^2)
SPACE Complexity - O(N)
"""

from string import ascii_lowercase
class Solution2:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S







# Approach 1
# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY - O(N-D)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        out = []
        
        for ch in s:
            if out and ch == out[-1]:
                out.pop()
            else:
                out.append(ch)
        
        return ''.join(out)
        
# Approach 2       
from string import ascii_lowercase

class Solution1:
    def removeDuplicates(self, S: str) -> str:
        
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            print("prev_length is {}".format(prev_length))
            for d in duplicates:
                S = S.replace(d, '')
            print("new prev_length and len(S) is {} and {}".format(prev_length, len(S)))

        return S
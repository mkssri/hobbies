from typing import List

# Approach 0

class Solution0:
    def reverseString(self, s):
        s.reverse()

# Approach 1: Recursive Approach 
# TIME Complexity - O(N) (To perform N/2 swaps)
# Space Complexity - O(N) (to keep the recursion track)

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # RECURSIVE APPROACH
        
        
        def helper(left, right):
            
            if left < right:
                
                s[left], s[right] = s[right], s[left]
        
                helper(left+1, right-1)
            
        helper(0, len(s)-1)


# Approach 2: Two Pointers, Iteration
# TIME Complexity - O(N) (To perform N/2 swaps)
# Space Complexity - O(1)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Two pointer approach
        
        left, right = 0, len(s)-1
        
        while left < right:
            
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
            
        print(s)
        return s
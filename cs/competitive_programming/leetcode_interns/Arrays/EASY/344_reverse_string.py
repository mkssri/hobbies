#!/usr/bin/python3


"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        start, end = 0, len(s)-1
        
        while start <= end:
            
            s[start], s[end] = s[end], s[start]
            
            start += 1
            end -= 1
            
        return s

if __name__ == "__main__":
    
    s= ["h","e","l","l","O"]
    obj = Solution()
    
    out = obj.reverseString(s)
    print("out is {}".format(out))
    
    
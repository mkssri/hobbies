#!/usr/bin/python3

# Link - https://leetcode.com/problems/reverse-words-in-a-string/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""
        
        s = s.strip().split(" ")

        print(s)

        while("" in s) :
            s.remove("")
        print(s)
        
        s= self.reverseList(s)
        
        for i in range(len(s)):
            out += s[i]
            
            if i != len(s)-1:
                out = out + " "
            
            
        return out    
    
    def reverseList(self, s):
        
        if len(s) == 0 or len(s) ==1:
            return s

        start, end = 0, len(s)-1

        while start <= end:

            s[start], s[end] = s[end], s[start]

            start += 1
            end -= 1

        return s
    
if __name__ == "__main__":
    
    obj = Solution()
    s = "a good   example"
    out = obj.reverseWords(s)
    print(out)
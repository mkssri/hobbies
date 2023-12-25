#!/usr/bin/python3

# Link - https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")
        out = ""
        s_new = []
        
        for x in s:
            print("x is {}".format(x))
            if x != '':
                s_new.append(x)
        rotate = len(s_new)
        for y in range(rotate-1,-1,-1):
                
                if y == 0:
                    out += s_new[y]
                else:
                    out += s_new[y]+" "
                    
        
        print("out is {}".format(out))
        return out
            
                
    
        
class Solution1(object):
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
#!/usr/bin/python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_str1 = self.returnDict(s)
        char_str2 = self.returnDict(t)
        
        if char_str1 == char_str2:
            return True
        else:
            return False
        
    
    def returnDict(self, s):
        
        char_str = [0]*26 # a-z character's 
        
        for x in range(0, len(s)):
            
            num = ord(s[x]) - ord('a')
            
            char_str[num] += 1
        
        return tuple(char_str)


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = self.returnDict(s)
        dict_t = self.returnDict(t)
        
        if dict_s == dict_t:
            return True
        else:
            return False
    
    def returnDict(self, s):
        
        dict_s = {}
        
        for x in range(0, len(s)):
            
            if s[x] in dict_s.keys():
                dict_s[s[x]] += 1
            else:
                dict_s[s[x]] = 1
            
        return dict_s
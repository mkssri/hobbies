#!/usr/bin/python3

# Link - https://leetcode.com/problems/string-transforms-into-another-string/

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        
        
        dict1 = {}
        
        if str1 == str2:
            return True
        
        if len(str1) != len(str2):
             return False
        
        dict1, set2 = {}, set()
        # dict1, set1 = {}, set()

        
        for x in range(0, len(str1)):
            
            # set1.add(str1[x])
            set2.add(str2[x])

    
            if str1[x] not in dict1.keys():
                dict1[str1[x]] = str2[x]
            
            elif str1[x] in dict1.keys() and dict1[str1[x]] != str2[x]:
                return False
        return len(set2) < 26
        # return len(set1) < 26
            
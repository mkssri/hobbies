#!/usr/bin/python3

"""
Time Complexity - O(N^2)
Space Complexity - O(N)
"""

class Solution:
    def groupAnagrams(self, strs):

        res = {}

        for s in strs:

            unique_key = self.uniqueKeyofStr(s)

            if unique_key in res.keys():
                res[unique_key].append(s)
            else:
                res[unique_key] = [s]
        
        return res.values()


    def uniqueKeyofStr(self, s):
        
        char_lst = [0] * 26

        for i in s:

            num = ord(i) - ord('a')
            char_lst[num] += 1
        
        return tuple(char_lst)


"""
Time Complexity - O(N^2LogN)
Space Complexity - O(N)
"""
class Solution1:
    def groupAnagrams(self, strs):

        if len(strs) == 1:
            return [strs]
            
        res = {}
        
        for ele in strs:
            tmp = list(ele)
            tmp.sort()
            tmp = ''.join(tmp)

            if tmp in res.keys():
                res[tmp].append(ele)
            else:
                res[tmp] = [ele]
        
        return res.values()
#!/usr/bin/python3


# https://leetcode.com/problems/group-anagrams/





from typing import DefaultDict


class Solution:
    def groupAnagrams(self, strs):

        if len(strs) == 1:
            return [strs]

        res = {}
        

        for ele in strs:

            lst = [0]*26
            
            for c in ele:

                val = ord(c) - ord('a')
                lst[val] += 1
            print(lst)
            lst = tuple(lst)
            print(lst)

            if lst in res.keys():
                res[lst].append(ele)
            else:
                res[lst] = [ele]
        
        return res.values()

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


# obj = Solution()
# strs = ["eat","tea","tan","ate","nat","bat"]

# out = obj.groupAnagrams(strs)

# print(out)

obj = Solution1()
strs = ["eat","tea","tan","ate","nat","bat"]

out = obj.groupAnagrams(strs)

print(out)

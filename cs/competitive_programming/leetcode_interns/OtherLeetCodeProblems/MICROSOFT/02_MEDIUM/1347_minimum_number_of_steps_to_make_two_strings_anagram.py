#!/usr/bin/python3

# Link - https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

# Solution - https://www.youtube.com/watch?v=hgBjY3KfLFc

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ans = 0
        
        m = {}
        
        for x in s:
            
            m[x] = 1 if x not in m.keys() else m[x]+1
        
        print("m is {}".format(m))
            
        for x in t:
            m[x] = -1 if x not in m.keys() else m[x]-1

        print("m is {}".format(m))

        for x in m.keys():
            
            ans = ans + abs(m[x])
        print("ans is {}".format(ans))
        
        return int(ans/2)

class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        
        if len(s) != len(t):
            return -1
        
        dict_s, dict_t = {}, {}
        
        for x in s:
            
            if x not in dict_s.keys():
                dict_s[x] = 1
            else:
                dict_s[x] += 1
                
        for y in t:
            
            if y not in dict_t.keys():
                dict_t[y] = 1
            else:
                dict_t[y] += 1
                
        
        print("dict_s - {}".format(dict_s))
        
        print("dict_t - {}".format(dict_t))
        
        if dict_t == dict_s:
            return 0
        
        count = 0
        for k in dict_s.keys():
            
            if k in dict_t.keys():
                
                count = count + abs(dict_s[k]-dict_t[k])
                del dict_t[k]
            else:
                count = count + dict_s[k]
                
        print("new dict_t - {}".format(dict_t))

                
        for k in dict_t.keys():
            
            count = count + dict_t[k]
        
                
        print("count is - {}".format(count))
        changes = int(count/2)
        print("so number of changes to do are - {}".format(changes))
        
        return changes
        
        
        

#!/usr/bin/python3

# Question - https://leetcode.com/problems/rotate-string/
# 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        
        for x in s:
            
            if x not in goal:
                return False
        
        
        val = goal[0]
        start_index = []
        
        for x in range(0,len(s)):
            
            if s[x] == val:
                start_index.append(x)
                
        for y in start_index:
            
            org_str = s
        
            for x in range(0,y):

                tmp = org_str[0]
                org_str = org_str[1:]
                org_str += tmp

            print("org_str value is - {}".format(org_str))

            if org_str == goal:
                return True
        
        return False
            
# Trick Solution
class Solution1:
    def rotateString(self, s: str, goal: str) -> bool:
        
        return len(s) == len(goal) and goal in s+s
#!/usr/bin/python3

# https://leetcode.com/problems/add-strings/

"""
Time Complexity - O(n)
Space Complexity - O(n)
"""


class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        
        carry, temp = 0, []

        i = len(num1) - 1
        j = len(num2) - 1
        
        while( i>=0 or j>=0 or carry > 0):
            
            s1 = 0 if i < 0 else int(num1[i])
            s2 = 0 if j < 0 else int(num2[j])
            
            total = s1 + s2 + carry

            
            carry, val = divmod(total, 10)
            
            temp.insert(0, val)

            print("carry3-{}, val-{}".format(carry, val))
            
            i -= 1
            j -= 1
        
            
        print("temp is {}".format(temp))
        out = ""
        for x in temp:
            out += str(x)
        
        return out
            
            

            
        
        
"""
Time Complexity - O(n)
Space Complexity - O(n)
""" 

class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # carry, temp = 0, []
        carry, temp = 0, ""

        i = len(num1) - 1
        j = len(num2) - 1
        
        while( i>=0 or j>=0 or carry > 0):
            
            s1 = 0 if i < 0 else int(num1[i])
            s2 = 0 if j < 0 else int(num2[j])
            
            total = s1 + s2 + carry

            
            carry, val = divmod(total, 10)
            
            temp = str(val) + temp

            print("carry3-{}, val-{}".format(carry, val))
            
            i -= 1
            j -= 1
        
        return temp
            

# Leetcode Solution

class Solution3:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
            

            
        
        
        
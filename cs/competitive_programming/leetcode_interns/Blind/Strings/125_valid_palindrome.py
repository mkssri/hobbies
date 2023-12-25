#!/usr/bin/python3

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        

        i, j = 0, len(s)-1
        
        while i < j:
            
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1
                
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True


"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        

        # Compare by reversing the string
        
        filtered_s = filter( lambda  ch: ch.isalnum(), s)
        filtered_s_lower = map( lambda ch: ch.lower(), filtered_s)

        filtered_s_lower = list(filtered_s_lower)
        filtered_s_lower_rev = filtered_s_lower[::-1]
        
        if filtered_s_lower == filtered_s_lower_rev:
            return True
        else:
            return False

"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""      

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Format String 
        s = self.strFormat(s)

        # Check if Palindrome
        
        i, j = 0, len(s)-1
        
        while i < j:
            
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            
            else:
                return False
        
        return True
    
    
    def strFormat(self, s):
        tmp = ""
        
        for x in s:
            
            if x.isalnum():
                
                if x.islower():
                    tmp += x
                else:
                    tmp += x.lower()
        return tmp


obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))

s = "A, a plan, a canal: Panama"
print(obj.isPalindrome(s))
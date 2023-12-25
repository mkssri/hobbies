class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:

            if c.isalnum():
                new_s += str(c.lower())
        
        s, e = 0, len(new_s)-1

        while( s<e ):

            if new_s[s] == new_s[e]:
                s += 1
                e -= 1
            else:
                return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)-1
        st, ed = 0, len(s)-1

        while(st<=ed):

            while(st<=l and not(s[st].isalnum())):
                st += 1
            while(0<=ed and not(s[ed].isalnum())):
                ed -= 1
            
            if(st>l and ed<0):
                break
            
            if(s[st].lower()==s[ed].lower()):
                st += 1
                ed -= 1
            else:
                return False
        return True

class Solution:
    def countSubstrings(self, s: str) -> int:

        res = list()

        def helper(s, l, r, res):
            while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
                p_str=s[l:r+1]
                res.append(p_str)
                l-=1
                r+=1
            return res
        
        for i in range(len(s)):
            #odd
            res = helper(s,i,i,res)
            #even
            res = helper(s,i,i+1,res)
        
        return len(res)
    
class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        def helper(s, l, r, res):
            while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
                res += 1
                l-=1
                r+=1
            return res
        
        for i in range(len(s)):
            #odd
            res=helper(s,i,i,res)
            #even
            res=helper(s,i,i+1,res)
        
        return res
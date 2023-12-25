class Solution:
    def longestPalindrome(self, s: str) -> str:

        def chkPalindrome(s, l, r, res, resL):

            while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
                if r-l+1>resL:
                    res=s[l:r+1]
                    resL=r-l+1
                r+=1
                l-=1
            return res, resL
        
        res, resL = "", 0
        for i in range(len(s)):
            res, resL= chkPalindrome(s,i,i,res,resL)
            res, resL= chkPalindrome(s,i,i+1,res,resL)
        return res
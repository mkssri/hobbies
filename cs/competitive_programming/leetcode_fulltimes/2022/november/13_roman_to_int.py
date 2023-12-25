class Solution:
    def romanToInt(self, s: str) -> int:

        store ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        res = 0
        for idx in range(len(s)-1):

            curr_val = store[s[idx]]
            nxt_val = store[s[idx+1]]

            if curr_val<nxt_val:
                res -= curr_val
            else:
                res += curr_val
        
        res += store[s[-1]]

        return res
import math

class Solution:
    def minSwaps(self, s: str) -> int:
        
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        if abs(ones-zeros) > 1:
            return -1

        cnt1, ans, cnt2 = 0, math.inf, 0
        if zeros >= ones:

            s1 = "01"*(n//2)

            if n//2:
                s1 += "0"

            for (c1,c) in zip(s1,s):

                if c1 != c:
                    cnt1 += 1
            
            ans = cnt1//2

        if ones >= zeros:

            s2 = "10"*(n//2)
            
            if n//2:
                s2 += "1"

            for (c2,c) in zip(s2,s):

                if c2 != c:
                    cnt2 += 1
            
            ans = min( cnt2//2, ans )
        
        return ans
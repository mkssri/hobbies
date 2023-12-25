import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r

        while(l<=r):

            m = l+(r-l)//2
            hrs = 0

            for p in piles:
                hrs += math.ceil(p/m)

            if hrs<=h:
                res = min(m, res)
                r=m-1
            else:
                l=m+1
        
        return res
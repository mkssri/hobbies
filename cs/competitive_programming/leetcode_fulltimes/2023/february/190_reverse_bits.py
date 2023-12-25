class Solution:
    def reverseBits(self, n: int) -> int:

        res=0
        d=0

        while(n>0):

            tmp = n&1
            res = res+(tmp<<(31-d))
            d += 1
            n = n>>1
        
        return res
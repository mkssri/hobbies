#!/usr/bin/python3

class Solution:

    def  countSetBits(self,n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count




obj = Solution()

out = obj.countSetBits(10)
print(out)




import collections
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        cur_sum = 0
        res = 0
        remainders = collections.defaultdict(int)
        remainders[0]=1

        for n in nums:
            cur_sum += n

            tmp = cur_sum%k

            if tmp in remainders:
                res += remainders[tmp]
            
            remainders[tmp] += 1
        
        return res
from typing import List
import math

class Solution:
    def minMoves(self, nums: List[int]) -> int:

        min_ele = math.inf

        for num in nums:
            min_ele = min(min_ele, num)
        res = 0
        for num in nums:
            res += num

        res -= (len(nums)*(min_ele))

        return res
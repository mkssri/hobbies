class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        pre, curr, _max = -1, 0, 0

        for x in range( len(nums) ):

            ele = nums[x]

            if ele == 0:
                pre, curr = curr, 0
            else:
                curr += 1

            _max = max( _max, pre+curr+1 )
        
        return _max
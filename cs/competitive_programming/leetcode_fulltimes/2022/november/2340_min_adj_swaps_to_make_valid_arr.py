class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        res = 0

        n = len(nums)
        min_val, Max_val = min(nums), max(nums)
        # min_idx, max_idx = nums.index(min_val), nums.index(Max_val)
        # use below since for case nums=[3,4,5,5,3,1], above gives max_idx of 2
        # where as in real life it will be 3, which will be given by below.
        min_idx, max_idx = nums.index(min_val), n-1-nums[::-1].index(Max_val)


        if min_idx == max_idx:
            return res
        elif min_idx < max_idx:
            return min_idx + n-1-max_idx
        else:
            return 2*(min_idx-max_idx)-1+max_idx+n-1-min_idx
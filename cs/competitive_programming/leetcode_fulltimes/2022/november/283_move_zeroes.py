class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)
        idx, cnt = 0, 0

        while( cnt < len_nums ):
            if( nums[idx] == 0 ):
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
            cnt += 1